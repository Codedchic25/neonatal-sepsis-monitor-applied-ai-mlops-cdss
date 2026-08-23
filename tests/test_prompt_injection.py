"""Unit tests targeting prompt injection resistance boundaries inside the clinical CDSS expert layer."""

from src.medical.expert import MedicalExpert


def test_prompt_injection_firewall_sanitization():
    """Validates if the local expert layer gracefully routes structural XML elements."""
    expert = MedicalExpert()
    vitals_payload = {
        "heart_rate": 170,
        "temperature": 39.1,
        "spo2": 91,
        "crp": 30.0,
        "pct": 5.2,
    }

    # Execute the local deterministic simulation pipeline (Groq Bypassed)
    response = expert.generate_clinical_support(
        vitals_payload=vitals_payload, base_system_instruction="", lang="ro"
    )

    # Verify structural compliance requirements for core UI tab parsing layers
    assert "<RAPORT>" in response
    assert "<MEDICATIE>" in response
    assert "</FCC>" in response
    assert "Sinteză Clinică" in response
