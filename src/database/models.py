"""SQLAlchemy Core Database Models for Neonatal Sepsis Telemetry.

Defines the relational schema used to store hourly vitals, biomarkers,
and active Family-Centered Care (FCC) therapeutic state parameters.
"""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Initialize the declarative base architecture for ORM entity mapping
Base = declarative_base()


class NeonatalTelemetry(Base):
    """Relational entity mapping schema for persistent infant clinical payloads."""

    __tablename__ = "neonatal_telemetry"

    # Transactional identity boundary tracking markers
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Biometric data scale parameter
    weight_kg = Column(Float, nullable=False, default=2.50)
    profile_name = Column(String(100), nullable=False, default="Term Neonate")

    # Real-time physiological telemetry vectors
    heart_rate = Column(Integer, nullable=False)
    temperature = Column(Float, nullable=False)
    systolic_bp = Column(Integer, nullable=False)
    diastolic_bp = Column(Integer, nullable=False)
    oxygen_saturation = Column(Float, nullable=False)  # SpO2 percentage

    # High-acuity biological inflammatory biomarkers
    pcr_level = Column(Float, nullable=False)  # C-Reactive Protein (mg/L)
    pct_level = Column(Float, nullable=False)  # Procalcitonin (ng/mL)

    # Active clinical renal physiology status scales
    aki_level = Column(String(50), nullable=False, default="normal")

    # Persistent Family-Centered Care (FCC) supportive modifiers
    kangaroo_care_active = Column(Boolean, nullable=False, default=False)
    nutrition_type_active = Column(String(50), nullable=False, default="None")
    music_therapy_active = Column(Boolean, nullable=False, default=False)

    # Treatment deployment vector parameters
    antibiotics_administered = Column(Boolean, nullable=False, default=False)
    sepsis_risk_score = Column(Float, nullable=False, default=0.0)
    sepsis_status_label = Column(String(50), nullable=False, default="Low Risk")

    def __repr__(self) -> str:
        """Returns a strict technical summary of the mapped clinical telemetry frame state."""
        return (
            f"<NeonatalTelemetry(id={self.id}, TS={self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}, "
            f"HR={self.heart_rate}, SepsisRisk={self.sepsis_risk_score}%, ABx={self.antibiotics_administered})>"
        )
