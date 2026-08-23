"""Clinical Telemetry Mock Data Generation Engine.

Populates the production database framework with standard high-acuity
NICU telemetry frames for system demonstrations and interface audits.
"""

from src.database.connection import get_db_session
from src.database.models import NeonatalTelemetry


def seed_mock_telemetry() -> None:
    """Injects a baseline high-acuity septic telemetry frame into the database layer."""
    print("🚀 Initializing mock neonatal data simulation sequence...")

    with get_db_session() as session:
        mock_frame = NeonatalTelemetry(
            heart_rate=175,
            temperature=38.9,
            systolic_bp=54,
            diastolic_bp=32,
            oxygen_saturation=94.0,
            pcr_level=25.0,
            pct_level=4.5,
            profile_name="Preterm 28w",
            aki_level="normal",
            sepsis_risk_score=95.0,
            sepsis_status_label="Critical Sepsis Risk",
        )
        session.add(mock_frame)

    print(
        "✅ SUCCESS: Mock telemetry payload successfully written into production database."
    )


if __name__ == "__main__":
    seed_mock_telemetry()
