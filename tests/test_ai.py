"""Unit tests targeting the local fail-safe clinical synthesis orchestration layer."""

from src.medical.expert import MedicalExpert


def test_ai_failsafe_deterministic_fallback():
    """Validates that the medical expert generates structured clinical output locally."""
    expert = MedicalExpert()
    vitals = {
        "heart_rate": 140,
        "temperature": 36.8,
        "spo2": 98,
        "crp": 4.2,
        "pct": 0.4,
    }

    response = expert.generate_clinical_support(
        vitals_payload=vitals, base_system_instruction="", lang="ro"
    )

    # Verificăm contractul de output structurat XML solicitat de dashboard
    assert "<RAPORT>" in response
    assert "<MEDICATIE>" in response
    assert "</FCC>" in response
    assert "Sinteză Clinică" in response
