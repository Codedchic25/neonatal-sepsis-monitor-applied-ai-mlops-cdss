"""Reconstructed baseline for neonatal telemetry schema.

Revision ID: 35ec0689bf29
Reconstructed from the live SQLite schema and SQLAlchemy metadata
because the original migration file is no longer present in Git.
"""

import sqlalchemy as sa
from alembic import op

# Revision identifiers, used by Alembic.
revision = "35ec0689bf29"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create the initial neonatal telemetry schema."""
    op.create_table(
        "neonatal_telemetry",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("weight_kg", sa.Float(), nullable=False),
        sa.Column("profile_name", sa.String(length=100), nullable=False),
        sa.Column("heart_rate", sa.Integer(), nullable=False),
        sa.Column("temperature", sa.Float(), nullable=False),
        sa.Column("systolic_bp", sa.Integer(), nullable=False),
        sa.Column("diastolic_bp", sa.Integer(), nullable=False),
        sa.Column("oxygen_saturation", sa.Float(), nullable=False),
        sa.Column("pcr_level", sa.Float(), nullable=False),
        sa.Column("pct_level", sa.Float(), nullable=False),
        sa.Column("aki_level", sa.String(length=50), nullable=False),
        sa.Column("kangaroo_care_active", sa.Boolean(), nullable=False),
        sa.Column(
            "nutrition_type_active",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column("music_therapy_active", sa.Boolean(), nullable=False),
        sa.Column(
            "antibiotics_administered",
            sa.Boolean(),
            nullable=False,
        ),
        sa.Column("sepsis_risk_score", sa.Float(), nullable=False),
        sa.Column(
            "sepsis_status_label",
            sa.String(length=50),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Remove the neonatal telemetry schema."""
    op.drop_table("neonatal_telemetry")
