"""NICU Sepsis Monitor AI - Clinical Retrieval-Augmented Generation (RAG) Engine.

Determinisitically binds official medical reference constants, gestational bounds,
and weight-based dosage guidelines straight into the active prompt workspace layer.
"""

import logging
from typing import Any

from src.medical.protocols import (
    EMPIRIC_ANTIBIOTIC_PROTOCOLS,
    get_clinical_gravity_label,
)

logger = logging.getLogger(__name__)


class NeonatalRAGEngine:
    """Retrieves institutional medical guidelines and injects them as a grounded context."""

    def __init__(self) -> None:
        """Initializes internal knowledge references for precise clinical support mapping."""
        self.protocols = EMPIRIC_ANTIBIOTIC_PROTOCOLS

    def generate_augmented_prompt(
        self, vitals: dict[str, Any], system_prompt: str, lang: str
    ) -> str:
        """Combines system behavioral instructions, reference guidelines, and live telemetry data.

        Args:
            vitals (dict): Live patient physiological metrics.
            system_prompt (str): Core operational rules and XML requirements.
            lang (str): Target localization language layout code.

        Returns:
            str: Fully augmented user instruction context ready for LLM processing.
        """
        # Extract biomarkers with safe defaults to calculate deterministic severity
        pcr_val = float(vitals.get("pcr_level", vitals.get("pcr", 0.0)))
        pct_val = float(vitals.get("pct_level", vitals.get("pct", 0.0)))

        # Pull the rule-based clinical classification label
        clinical_guideline_label = get_clinical_gravity_label(pcr_val, pct_val)

        # Assemble the grounded protocol text block based on official guidelines
        knowledge_context = (
            f"[OFFICIAL INSTITUTIONAL GUIDELINE CONTEXT]:\n"
            f"- Clinical Severity Stratification: {clinical_guideline_label}\n"
            f"- Standard Initial Empiric Antibiotic Protocols:\n"
            f"  * Ampicillin Target: {self.protocols['Ampicillin']['target']}\n"
            f"  * Gentamicin Target: {self.protocols['Gentamicin']['target']}\n"
        )

        # Compile everything into a single synchronized payload sequence
        return (
            f"{system_prompt}\n\n"
            f"{knowledge_context}\n\n"
            f"[LIVE TELEMETRY STREAM TO ANALYZE]:\n"
            f"- Targeted Patient Vitals Data: {vitals}\n"
            f"- Operational Target Output Language: {lang}\n"
        )
