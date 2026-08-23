"""Neonatal Clinical Risk Stratification and Vital Signs Evaluator.

This module executes rule-based clinical boundary validation on physiological
telemetry vectors to detect homeostatic anomalies such as neonatal tachycardia,
hyperthermia, hypotension, and automated composite sepsis risk scores.
"""

from typing import Any


def evaluate_vital_signs(
    heart_rate: int,
    temperature: float,
    systolic_bp: int,
    diastolic_bp: int,
    oxygen_saturation: float,
) -> dict[str, Any]:
    """Evaluates individual neonatal vital signs against strict NICU clinical thresholds.

    Args:
        heart_rate (int): Heart rate in beats per minute (bpm).
        temperature (float): Core body temperature in degrees Celsius (°C).
        systolic_bp (int): Systolic blood pressure in mmHg.
        diastolic_bp (int): Diastolic blood pressure in mmHg.
        oxygen_saturation (float): Blood oxygen saturation percentage (SpO2).

    Returns:
        dict[str, Any]: A dictionary containing active boolean alerts and descriptive text strings.
    """
    # Evaluate boolean flags once to prevent redundant execution blocks
    is_tachycardia = heart_rate > 160
    is_hyperthermia = temperature > 37.5
    is_hypotension = systolic_bp < 45 or diastolic_bp < 25
    is_hypoxemia = oxygen_saturation < 90

    # Standard NICU clinical boundary markers for a 28-week preterm/term infant
    alerts = {
        "tachycardia": {
            "active": is_tachycardia,
            "label": "Tachycardia" if is_tachycardia else "Normal",
            "status": "danger" if is_tachycardia else "success",
        },
        "hyperthermia": {
            "active": is_hyperthermia,
            "label": "Hyperthermia" if is_hyperthermia else "Normothermia",
            "status": "danger" if is_hyperthermia else "success",
        },
        "hypotension": {
            "active": is_hypotension,
            "label": "Hypotension" if is_hypotension else "Normotension",
            "status": "danger" if is_hypotension else "success",
        },
        "hypoxemia": {
            "active": is_hypoxemia,
            "label": "Hypoxemia" if is_hypoxemia else "Target Oxygenation",
            "status": "danger" if is_hypoxemia else "success",
        },
    }

    return alerts


def calculate_sepsis_risk_score(
    alerts: dict[str, Any], pcr_level: float, pct_level: float
) -> dict[str, Any]:
    """Computes a multi-parametric clinical risk score for neonatal sepsis tracking.

    Combines real-time stochastic vital sign anomalies with laboratory biomarker
    clearance baselines to output an enterprise-grade risk stratification payload.

    Args:
        alerts (dict[str, Any]): Dictionary of physiological alerts from evaluate_vital_signs.
        pcr_level (float): C-Reactive Protein concentration in mg/L.
        pct_level (float): Procalcitonin concentration in ng/mL.

    Returns:
        dict[str, Any]: Categorized risk status and raw numerical score payload.
    """
    score = 0

    # Accumulate points based on active vital sign alerts (Weight: 2 points each)
    if alerts["tachycardia"]["active"]:
        score += 2
    if alerts["hyperthermia"]["active"]:
        score += 2
    if alerts["hypotension"]["active"]:
        score += 2
    if alerts["hypoxemia"]["active"]:
        score += 1

    # Accumulate points based on inflammatory biomarker thresholds (Weight: 3 and 4 points)
    if pcr_level >= 10.0:
        score += 3
    if pct_level >= 2.0:
        score += 4  # Procalcitonin has higher clinical specificity for bacterial sepsis

    # Stratify clinical gravity bands aligned with system notification layers
    if score >= 7:
        status = "Critical Sepsis Risk"  # ALIGNED: Matches Twilio emergency string matching criteria
        color = "red"
    elif score >= 3:
        status = "Moderate Risk"
        color = "orange"
    else:
        status = "Low Risk"
        color = "green"

    return {
        "raw_score": score,
        "status": status,
        "color": color,
        "requires_antibiotics": score >= 3,
    }
