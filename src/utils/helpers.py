"""Clinical Utility Helpers and Mathematical String Formatters.

Provides clean string manipulators, rounding utilities, and base64
sandbox encoders tailored for ReportLab and Streamlit components.
"""

import base64


def format_blood_pressure(systolic: int, diastolic: int) -> str:
    """Formats raw blood pressure integer values into standard clinical strings."""
    return f"{systolic}/{diastolic} mmHg"


def get_pdf_download_link(pdf_bytes: bytes, filename: str, link_text: str) -> str:
    """Generates a secure in-memory Base64 download anchor tag link for PDF files."""
    b64_pdf = base64.b64encode(pdf_bytes).decode()
    return f'<a href="data:application/pdf;base64,{b64_pdf}" download="{filename}" class="download-btn">{link_text}</a>'
