"""UI Dictionary and Multilingual Localization Matrix.

Provides centralized dictionary tokens to ensure absolute language decoupling
across layout headers, clinical alerts, and system state variables.
"""

from typing import Final

LOCALIZATION_MATRIX: Final[dict[str, dict[str, str]]] = {
    "RO": {
        "title": "🗺️ Sepsis Monitor AI — NICU CDSS Platform",
        "sidebar_hdr": "Configuration Panel / Panou Configurare",
        "role_select": "🌐 Select Clinical Role / Rol Clinic",
        "weight_input": "Newborn Weight / Greutate Nou-nascut (kg)",
        "execute_step": "Executa Pas Telemetric (Simulare Timp +1h)",
        "inject_therapy": "Injecteaza Schema Empirica (Ampicillina + Gentamicina)",
        "reset_profile": "Reseteaza Profil Clinic (Sterge Istoric DB)",
        "vitals_hdr": "🧠 Parametri Vitali in Timp Real",
        "hr_label": "Ritm Cardiac",
        "temp_label": "Temperatura",
        "spo2_label": "Saturatie O2",
        "bp_label": "Tensiune (SYS/DIA)",
        "critical_banner": "ALERTA SEPSIS CRITICA: Scor Risc >= 90%!",
        "stable_banner": "Status Telemetric Stabil — Monitorizare Standard NICU",
    },
    "EN": {
        "title": "🗺️ Sepsis Monitor AI — NICU CDSS Platform",
        "sidebar_hdr": "Configuration Panel",
        "role_select": "🌐 Select Clinical Role",
        "weight_input": "Newborn Weight (kg)",
        "execute_step": "Execute Telemetry Step (Time Simulation +1h)",
        "inject_therapy": "Inject Empirical Therapy (Ampicillin + Gentamicin)",
        "reset_profile": "Reset Clinical Profile (Wipe DB History)",
        "vitals_hdr": "🧠 Real-Time Physiological Vitals",
        "hr_label": "Heart Rate",
        "temp_label": "Core Temperature",
        "spo2_label": "Oxygen Saturation (SpO2)",
        "bp_label": "Blood Pressure (SYS/DIA)",
        "critical_banner": "CRITICAL SEPSIS RISK ALERT: Score >= 90%!",
        "stable_banner": "Stable Telemetry Status — Standard NICU Pathway",
    },
}
