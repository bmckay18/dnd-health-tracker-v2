from pathlib import Path

base_path = Path(__file__).resolve().parent
usp_path = base_path / "db" / "procedures"

## Database Environments
# healthDB.db = PROD
# healthDB_DEV.db = DEV
env_flag = 0 # 0 = dev, 1 = prod
if env_flag == 0:
    database_name = 'healthDB_DEV.db'
elif env_flag == 1:
    database_name = 'healthDB.db'