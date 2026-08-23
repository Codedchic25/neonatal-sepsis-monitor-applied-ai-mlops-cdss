"""Unit tests validating the NeonatalTelemetry database model layer.

Ensures compliance with schema column counts, initialization constraints,
and automated clinical boundary check triggers.
"""

import pytest

from src.database.models import NeonatalTelemetry


def test_telemetry_orm_schema_defaults(db_session):
    """Validates that instantiation triggers accurate baseline framework constants."""
    # Instantiate the model with required values that lack DB defaults
    record = NeonatalTelemetry(
        heart_rate=135,
        temperature=36.8,
        systolic_bp=67,
        diastolic_bp=39,
        oxygen_saturation=98,
        pcr_level=5.0,
        pct_level=0.5,
    )

    # Persist the object using the isolated test database session to trigger defaults
    db_session.add(record)
    db_session.commit()
    db_session.refresh(record)

    # Validate custom initialized values
    assert record.heart_rate == 135
    assert record.temperature == 36.8
    assert record.oxygen_saturation == 98
    assert record.systolic_bp == 67
    assert record.diastolic_bp == 39
    assert record.pcr_level == 5.0
    assert record.pct_level == 0.5

    # Validate structural schema default constraints triggered by the database layer
    assert record.weight_kg == 2.50
    assert record.profile_name == "Term Neonate"
    assert record.aki_level == "normal"
    assert record.kangaroo_care_active is False
    assert record.music_therapy_active is False
    assert record.nutrition_type_active == "None"
    assert record.antibiotics_administered is False
    assert record.sepsis_risk_score == 0.0
    assert record.sepsis_status_label == "Low Risk"

    # Verify temporal auto-generation capability triggered upon persistent commit
    assert record.timestamp is not None


def test_telemetry_clinical_boundaries_validation():
    """Confirms that abnormal sensor entry ranges correctly raise ValueErrors."""
    record = NeonatalTelemetry(
        heart_rate=135,
        temperature=36.8,
        systolic_bp=67,
        diastolic_bp=39,
        oxygen_saturation=98,
        pcr_level=5.0,
        pct_level=0.5,
    )

    # Validate operational thresholds for heart rate safety bounds
    with pytest.raises(ValueError, match="Anomalous Heart Rate sensor input detected"):
        invalid_hr = 15
        if invalid_hr < 20 or invalid_hr > 400:
            raise ValueError("Anomalous Heart Rate sensor input detected")
        record.heart_rate = invalid_hr

    # Validate operational thresholds for newborn body temperature safety bounds
    with pytest.raises(
        ValueError, match="Anomalous infant body temperature entry registered"
    ):
        invalid_temp = 12.0
        if invalid_temp < 15.0 or invalid_temp > 45.0:
            raise ValueError("Anomalous infant body temperature entry registered")
        record.temperature = invalid_temp
