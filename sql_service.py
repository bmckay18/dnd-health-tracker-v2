import sqlite3 as s
from config import *

class SQLService():
    DB_FILE_NAME = DB_NAME

    def __init__(self):
        self.db_schema = BASE_PATH / "db" / "schema.sql"

    def execute_insert(self, query, return_flag: int = 0): # Used for insert queries
        conn = s.connect(self.DB_FILE_NAME)
        cursor = conn.cursor()
        try:
            if return_flag == 0:
                cursor.executescript(query)
                conn.commit()
            elif return_flag == 1:
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
        conn = s.connect(self.DB_FILE_NAME)
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
        conn = s.connect(self.DB_FILE_NAME)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows 
        except Exception as m:
            raise Exception(f"An error occurred: {m}")
        finally:
            conn.close()
    
    def create_db(self):
        with s.connect(self.DB_FILE_NAME) as conn:
            with open(self.db_schema, 'r') as f:
                conn.executescript(f.read())