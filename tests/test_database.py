"""Unit tests verifying local SQLite database schema bindings and column structural migrations."""

import sqlite3


def test_sqlite_telemetry_table_schema_integrity():
    """Verifies that the runtime relational SQLite telemetry table complies with active CDSS inputs."""
    conn = sqlite3.connect("sepsis_neonatal.db")
    cursor = conn.cursor()

    # Extract column array structural profiles using internal PRAGMA schemas
    cursor.execute("PRAGMA table_info(telemetry);")
    columns_raw = cursor.fetchall()
    conn.close()

    column_names = [col[1] for col in columns_raw]

    assert "heart_rate" in column_names
    assert "temperature" in column_names
    assert "crp" in column_names
    assert "renal_status" in column_names
