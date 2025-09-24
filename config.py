from pathlib import Path

base_path = Path(__file__).resolve().parent
usp_path = base_path / "db" / "procedures"

## Database Environments
# healthDB.db = PROD
# healthDB_DEV.db = DEV
envFlag = 0 # 0 = dev, 1 = prod
if envFlag == 0:
    database_name = 'healthDB_DEV.db'
elif envFlag == 1:
    database_name = 'healthDB.db'