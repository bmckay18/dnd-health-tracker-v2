from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
USP_PATH = BASE_PATH / "db" / "procedures"

## Database Environments
# healthDB.db = PROD
# healthDB_DEV.db = DEV
ENV_FLAG = 0 # 0 = dev, 1 = prod
if ENV_FLAG == 0:
    db_name = 'healthDB_DEV.db'
elif ENV_FLAG == 1:
    db_name = 'healthDB.db'