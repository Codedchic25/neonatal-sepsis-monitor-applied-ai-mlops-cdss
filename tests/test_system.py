"""Integration tests verifying core system workflow boundaries and local telemetry storage."""

import sqlite3


def test_system_sqlite_insertion_and_retrieval():
    """Validates integration lifecycle by committing and fetching real-time clinical parameters."""
    conn = sqlite3.connect("sepsis_neonatal.db")
    cursor = conn.cursor()

    # Inserăm un pas de test determinist în baza de date locală
    cursor.execute(
        """
        INSERT INTO telemetry (timestamp, heart_rate, temperature, oxygen_saturation, blood_pressure, crp, pct)
        VALUES ('23:15:00', 142, 36.9, 97, '64/41 mmHg', 4.5, 0.42)
    """
    )
    conn.commit()

    # Validăm dacă sistemul poate recupera corect ultima telemetrie înregistrată
    cursor.execute(
        "SELECT heart_rate, temperature FROM telemetry ORDER BY id DESC LIMIT 1;"
    )
    last_step = cursor.fetchone()
    conn.close()

    assert last_step is not None
    assert last_step[0] == 142
    assert last_step[1] == 36.9
