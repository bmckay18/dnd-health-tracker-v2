import sqlService as s
from pathlib import Path

base_path = Path(__file__).resolve().parent
sql_conn = s.SQLService()

sql_conn.create_db() # Create the DB

# Extract seed schema
with open(base_path / "db" / "seed.sql") as f:
    seed = f.read()

try:
    sql_conn.execute_insert(seed)
    print('Database Populated Successfully')
except Exception as m:
    print('Database Population Failed')
    print(m)