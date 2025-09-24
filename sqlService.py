import sqlite3 as s
from config import *

class SQLService():
    db_filename = database_name

    def __init__(self):
        self.db_schema = base_path / "db" / "schema.sql"

    def execute_insert(self, query, returnFlag: int = 0): # Used for insert queries
        conn = s.connect(self.db_filename)
        cursor = conn.cursor()
        try:
            if returnFlag == 0:
                cursor.executescript(query)
                conn.commit()
            elif returnFlag == 1:
                cursor.execute(query)
                last_id = cursor.lastrowid
                conn.commit()
                return last_id
        except Exception as m:
            conn.rollback()
            raise Exception(f"An error occurred: {m}")
        finally:
            conn.close()
    
    def execute_update(self, query): # Used for update queries
        conn = s.connect(self.db_filename)
        cursor = conn.cursor()
        try:
            cursor.executescript(query)
            conn.commit()
        except Exception as m:
            conn.rollback()
            raise Exception(f"An error occurred: {m}")
        finally:
            conn.close()
    
    def execute_select(self, query): # Used for select queries
        conn = s.connect(self.db_filename)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows 
        except Exception as m:
            raise Exception(f"An error occurred: {m}")
        finally:
            conn.close()
    
    def CreateDB(self):
        with s.connect(self.db_filename) as conn:
            with open(self.db_schema, 'r') as f:
                conn.executescript(f.read())