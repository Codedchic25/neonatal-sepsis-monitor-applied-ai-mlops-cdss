"""Clinical Environment Hard System Reset Utility.

Purges the active localized SQLite relational file to force a clean metadata
bootstrap and create empty telemetry histories for incoming shifts.
"""

import os


def reset_system_database() -> None:
    """Safely purges the target production database file from the host filesystem."""
    # RECTIFICAT: Aliniat cu numele bazei de date neonatale din .env
    target = "sepsis_neonatal.db"
    if os.path.exists(target):
        try:
            os.remove(target)
            print(
                f"✅ SUCCESS: Relational database [{target}] cleared from host filesystem."
            )
        except OSError as e:
            print(f"⚠️ OS EXCEPTION: Database file is locked or unreachable: {e!s}")
    else:
        print(f"ℹ️ INFO: Target database [{target}] is already clear or unallocated.")


if __name__ == "__main__":
    reset_system_database()
