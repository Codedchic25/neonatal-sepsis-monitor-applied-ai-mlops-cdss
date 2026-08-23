"""Automated Production Database Backup Utility.

Extracts timestamps and duplicates the active SQLite database binary
into the persistent isolated storage backups directory frame safely.
"""

import datetime
import os
import shutil


def backup_db() -> None:
    """Executes a safe binary copy operation of the active clinical database file."""
    # RECTIFICAT: Aliniat cu numele bazei de date neonatale din .env
    source = "sepsis_neonatal.db"
    if not os.path.exists(source):
        print(f"⚠️ BACKUP EXCEPTION: Target source database [{source}] does not exist.")
        return

    backups_dir = os.path.join("database", "backups")
    os.makedirs(backups_dir, exist_ok=True)

    # RECTIFICAT: Sintaxă aliniată la bunele practici timezone-aware pentru Python 3.11+
    timestamp = datetime.datetime.now(tz=datetime.UTC).strftime("%Y%m%d_%H%M%S")
    destination = os.path.join(backups_dir, f"sepsis_neonatal_backup_{timestamp}.db")

    try:
        shutil.copy2(source, destination)
        print(f"✅ SUCCESS: Database backup archived seamlessly -> {destination}")
    except Exception as e:  # noqa: BLE001
        print(f"⚠️ CRITICAL INFRASTRUCTURE FAULT: Backup execution failed: {e!r}")


if __name__ == "__main__":
    backup_db()
