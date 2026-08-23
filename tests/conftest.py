"""Global Pytest Configuration and Common Isolated Test Fixtures.

This module provisions thread-safe, context-managed in-memory database engines
and active transactional sessions to isolate unit and integration tests from
the production data layer.
"""

import sqlite3
from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.database.models import Base

# --- AUTOMATED GITHUB ACTIONS FALLBACK DATABASE INITIALIZATION ---
# Forces the creation of the physical SQLite database file required by local system tests
_conn = sqlite3.connect("sepsis_neonatal.db")
_cursor = _conn.cursor()
_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        heart_rate INTEGER,
        temperature REAL,
        oxygen_saturation INTEGER,
        blood_pressure TEXT,
        crp REAL,
        pct REAL
    );
"""
)
_conn.commit()
_conn.close()
# -----------------------------------------------------------------

# Setup an isolated, high-performance in-memory relational database configuration
TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="session")
def test_engine() -> Generator[create_engine, None, None]:
    """Provisions a single shared SQLAlchemy relational database execution engine."""
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session(test_engine) -> Generator[Session, None, None]:
    """Supplies an isolated, transaction-rolled database session for individual test execution."""
    connection = test_engine.connect()
    transaction = connection.begin()

    testing_session_factory = sessionmaker(
        bind=connection, autoflush=False, autocommit=False
    )
    session = testing_session_factory()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
