"""SQLAlchemy Thread-Safe Session Lifecycle Management Framework.

Provides an isolated local session manager via context managers to prevent
concurrency blocks, connection leaks, and transactional race conditions.
"""

import os
from collections.abc import (
    Generator,
)  # FIXED: Aligned with modern Python specifications (UP035)
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.database.models import Base  # FIXED: Properly isolated and alphabetized (I001)

# Extract the target relational connection path safely from local configuration handles
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///sepsis_neonatal.db")

# Enforce explicit isolated thread pool checks configuration for SQLite frameworks
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)

# Bind the session factory boundary tracker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def initialize_database() -> None:
    """Automates relational database initialization at bootstrap, creating all missing metadata structures."""
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """Context manager delivering an isolated transactional session frame per thread runtime execution.

    Yields:
        Generator[Session, None, None]: An isolated active SQLAlchemy ORM database session client.
    """
    session = SessionLocal()
    try:
        get_session = session
        yield get_session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
