from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from core.database import Base
from core.config import settings

# ⬇️ IMPORT ALL MODELS (THIS IS REQUIRED)
from models.user import User
from models.notification import Notification
from models.common import Audit

config = context.config

if config.config_file_name:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def get_url():
    return (
        f"postgresql://{settings.database_username}:"
        f"{settings.database_password}@{settings.database_hostname}:"
        f"{settings.database_port}/{settings.database_name}"
    )

def run_migrations_offline():
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": get_url()},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
