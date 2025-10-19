from pathlib import Path
from dotenv import load_dotenv
import os

# Static environment variables
BASE_PATH = Path(__file__).resolve().parent
USP_PATH = BASE_PATH / "db" / "procedures"

# Load environment variables from .env file
env = os.getenv("APP_ENV","dev")
if env == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

DB_NAME = os.getenv("DATABASE_NAME")