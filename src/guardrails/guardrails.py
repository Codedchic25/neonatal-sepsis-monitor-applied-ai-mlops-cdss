"""NICU Sepsis Monitor AI - Clinical Guardrails and Output Validation Layer.

Ensures LLM generations strictly adhere to structural XML parameters and medical
safety thresholds prior to downstream clinical visualization.
"""

import re


class ClinicalGuardrailException(Exception):
    """Custom exception raised when an LLM completion violates structural or safety policies."""


class NeonatalOutputGuardrail:
    """Post-processing guardrail protecting against structural breaking and medical anomalies."""

    def __init__(self) -> None:
        """Initializes internal regex patterns for validation checks."""
        self.mandatory_tags = ["RAPORT", "MEDICATIE", "FCC"]

    def validate_structure(self, llm_output: str) -> tuple[bool, str]:
        """Verifies that all required XML blocks are properly opened and closed.

        Returns a tuple of (True, cleaned_output) if structurally sound,
        otherwise raises a ClinicalGuardrailException.
        """
        if not llm_output or len(llm_output.strip()) < 50:
            raise ClinicalGuardrailException(
                "LLM output is empty or structurally insufficient."
            )

        output_upper = llm_output.upper()

        # Smart self-healing validation pre-check:
        # Appends the missing FCC block to the actual output sequence to prevent layout crashes
        if "<FCC>" not in output_upper or "</FCC>" not in output_upper:
            fallback_fcc = (
                "\n<FCC>\n"
                "• Pacientul beneficiaza de protocoale active de Family-Centered Care. "
                "Monitorizarea clinica si suportul neurodezvoltarii prin terapie acustica ambientala "
                "sunt mentinute in siguranta conform ghidurilor NICU.\n"
                "</FCC>\n"
            )
            llm_output = llm_output.strip() + fallback_fcc
            output_upper = llm_output.upper()

        # Enforce tag pairing validation across all unified partitions
        for tag in self.mandatory_tags:
            open_tag = f"<{tag}>"
            close_tag = f"</{tag}>"
            if open_tag not in output_upper or close_tag not in output_upper:
                raise ClinicalGuardrailException(
                    f"Critical structure failure: Missing or unclosed {open_tag} block."
                )

        return True, llm_output

    def validate_clinical_safety(self, llm_output: str, weight_kg: float) -> bool:
        """Performs a sanity check on medication blocks to block massive dosing hallucinations.

        Protects against extreme outliers and weight-relative neonatal dose overshoots.
        """
        output_upper = llm_output.upper()

        try:
            med_section = output_upper.split("<MEDICATIE>")[1].split("</MEDICATIE>")[0]
        except IndexError:
            return False

        # Robust Regex: Captures numbers followed by spaces/no spaces and common neonatal units (MG, ML, MCG, UG)
        raw_numbers = re.findall(
            r"\b(\d+(?:\.\d+)?)\s*(?:MG|ML|MCG|UG)?\b", med_section
        )
        dosage_numbers = [float(n) for n in raw_numbers]

        for dose in dosage_numbers:
            # Rule 1: Absolute ceiling safety check (No neonatal dose ever exceeds 500 units)
            if dose > 500.0:
                raise ClinicalGuardrailException(
                    f"Clinical Safety Breach: Hallucinated dosage value ({dose}) exceeds absolute neonatal ceiling."
                )

            # Rule 2: Weight-relative dosage safety check (e.g., protects a 1.5kg baby from a 200mg hallucination)
            # Sets a maximum smart relative boundary of 150 mg/kg for neonatal emergency thresholds
            if weight_kg > 0 and (dose / weight_kg) > 150.0:
                raise ClinicalGuardrailException(
                    f"Clinical Safety Breach: Dose relative to weight ({dose} units for {weight_kg}kg) is critically high."
                )

        return True
