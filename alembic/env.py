from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Основна метадана для моделей SQLAlchemy
from models import Base 

from your_module import Base, Group, Student, Teacher, Subject, Grade

config = context.config
target_metadata = Base.metadata
fileConfig(config.config_file_name)

connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool,
)

def run_migrations_online():
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

