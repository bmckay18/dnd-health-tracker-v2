# Define libraries
from sql_service import SQLService
from functions.extract_query import extract_query
import random as r

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

        return self.conn.execute_select(query)
    
    def generate_loot(self, amount: int = 1):
        items = []

        for i in range(0, amount):
            roll = r.randint(1, 100)
            item = next((key for key, value in self.loot_table if value >= roll), None)
            items.append(item)
        
        return items 