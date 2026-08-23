import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# Import the declarative Base from your real models layer for automated column detection
from src.database.models import Base

# This is the Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Interpret the config file for Python standard logging if present
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the target metadata directly to your active application core models
target_metadata = Base.metadata


def include_object(object_, name, type_, reflected, compare_to):
    """Exclude legacy database objects that are intentionally unmanaged."""
    return not (
        type_ == "table" and name == "telemetry" and reflected and compare_to is None
    )


# Dynamic runtime injection of the database path extracted safely from environment variables
db_url = os.getenv("DATABASE_URL", "sqlite:///sepsis_neonatal.db")
config.set_main_option("sqlalchemy.url", db_url)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode without an active live database connection handle."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        include_object=include_object,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode by connecting directly to the target database engine."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
        )


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
