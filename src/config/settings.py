"""Global Infrastructure Configuration and Environment Settings.

Centralizes environment token extraction, system database paths, and
low-latency hardware specifications for the inference model routing.
"""

import os
from typing import Final


class AppSettings:
    """Enterprise-grade application configuration vault mapping environment keys safely."""

    # API Cryptographic Token Keys
    GROQ_API_KEY: Final[str | None] = os.getenv("GROQ_API_KEY")
    TWILIO_ACCOUNT_SID: Final[str | None] = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN: Final[str | None] = os.getenv("TWILIO_AUTH_TOKEN")

    # Aliniat cu structura din .env (Înlocuit TWILIO_FROM_NUMBER)
    TWILIO_CLINICAL_PHONE: Final[str | None] = os.getenv("TWILIO_CLINICAL_PHONE")
    TWILIO_TWILIO_PHONE: Final[str | None] = os.getenv("TWILIO_TWILIO_PHONE")

    # Persistent Storage Parameters
    DATABASE_URL: Final[str] = os.getenv("DATABASE_URL", "sqlite:///sepsis_neonatal.db")

    # Low-latency Hardware Model Routing specifications
    # Citește din .env sau face fallback pe modelul tău instant 8B
    MODEL_CORE: Final[str] = os.getenv("GROQ_MODEL_NAME", "llama-3.1-8b-instant")
    TEMPERATURE: Final[float] = 0.1
    MAX_TOKENS: Final[int] = 1024
