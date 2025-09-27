import sql_service as s
from config import BASE_PATH

sql_conn = s.SQLService()
sql_conn.create_db() # Create the DB

# Extract seed schema
with open(BASE_PATH / "db" / "seed.sql") as f:
    seed = f.read()

try:
    sql_conn.execute_insert(seed)
    print('Database Populated Successfully')
except Exception as m:
    print('Database Population Failed')
    print(m)