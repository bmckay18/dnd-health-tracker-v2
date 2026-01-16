from pathlib import Path
from dotenv import load_dotenv
import os

# Static environment variables
BASE_PATH = Path(__file__).resolve().parent
USP_PATH = BASE_PATH / "db" / "procedures"

# Load environment variables from .env file
load_dotenv(".env")
ENV = os.getenv("APP_ENV", "dev")
DB_NAME = os.getenv("DATABASE_NAME", "npc_health.db")

if not DB_NAME:
    raise RuntimeError("DATABASE_NAME environment variable must be defined.")
elif DB_NAME == "npc_health.db":
    print('WARNING: Using local database')