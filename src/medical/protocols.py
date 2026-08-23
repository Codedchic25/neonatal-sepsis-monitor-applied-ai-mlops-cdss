"""NICU Clinical Protocols and Medical Reference Constants.

Houses official clinical threshold mappings, diagnostic boundary definitions,
and mandated empiric antibiotic dosing regimens for neonatal sepsis management,
stratified by gestational age indices.
"""

from typing import Any, Final

# --- SEPSIS CLINICAL ALARM BOUNDARIES ---
HEART_RATE_TACHYCARDIA_THRESHOLD: Final[int] = 160
"""Heart rate boundary in beats per minute (bpm) defining neonatal tachycardia."""

TEMPERATURE_HYPERTHERMIA_THRESHOLD: Final[float] = 37.5
"""Core body temperature boundary in degrees Celsius (°C) defining hyperthermia."""

TEMPERATURE_HYPOTHERMIA_THRESHOLD: Final[float] = 36.0
"""Core body temperature boundary in degrees Celsius (°C) defining hypothermia."""

OXYGEN_SATURATION_CRITICAL_THRESHOLD: Final[float] = 90.0
"""Oxygen saturation lower bound percentage (SpO2) triggering hypoxic status alerts."""

# --- CRITICAL BIOMARKER DIAGNOSTIC THRESHOLDS ---
CRP_CRITICAL_LIMIT: Final[float] = 15.0
"""C-Reactive Protein (PCR) critical threshold in mg/L indicating high inflammatory response.
Aligned with the primary application stability monitoring matrix.
"""

PCT_CRITICAL_LIMIT: Final[float] = 2.0
"""Procalcitonin (PCT) critical threshold in ng/mL indicating severe bacterial infection."""

# --- PHARMACOTHERAPY DOSING MAPS ---
EMPIRIC_ANTIBIOTIC_PROTOCOLS: Final[dict[str, dict[str, Any]]] = {
    "Ampicillin": {
        "dosage_mg_kg": 100.0,
        "route": "IV (Intravenous)",
        "frequency_hours": 12,
        "target": "Gram-positive coverage (Listeria, Group B Streptococcus)",
    },
    "Gentamicin": {
        "dosage_mg_kg": 4.0,
        "route": "IV (Intravenous)",
        "frequency_hours": 24,
        "target": "Gram-negative synergy coverage (Escherichia coli, Pseudomonas)",
    },
}


def get_clinical_gravity_label(pcr_level: float, pct_level: float) -> str:
    """Classifies the inflammatory severity band based on diagnostic biomarker values.

    Args:
        pcr_level (float): C-Reactive Protein concentration in mg/L.
        pct_level (float): Procalcitonin concentration in ng/mL.

    Returns:
        str: Categorized medical status rating ('Normal', 'Moderate Inflammation',
            or 'Critical Sepsis Indication').
    """
    if pcr_level > CRP_CRITICAL_LIMIT or pct_level > PCT_CRITICAL_LIMIT:
        return "Critical Sepsis Indication"
    if pcr_level > 2.0 or pct_level > 0.5:
        return "Moderate Inflammation"
    return "Normal"
