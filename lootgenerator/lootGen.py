# Define libraries
from config import *
from sql_service import SQLService
from functions.extract_query import extract_query

# This module will handle the logic for generating the loot

# Define class
class LootGen():
    def __init__(self, loot_table: int):
        self.conn = SQLService()
        self.loot_table_id = loot_table
        self.loot_table = self._get_loot_items()
    
    def _get_loot_items(self):
        query = extract_query('uspRetrieveLootTableFromID')
        query = query % (self.loot_table_id) # Replace placeholder with magic table

        return self.conn.execute_update(query)