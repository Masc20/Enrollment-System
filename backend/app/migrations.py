from alembic import command
from alembic.config import Config
import os

def run_migrations():
    # path to alembic.ini (relative to project root)
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "..", "alembic.ini"))
    alembic_cfg.set_main_option("script_location", "backend/alembic")

    command.upgrade(alembic_cfg, "head")