# Define libraries
from sql_service import SQLService
from functions import extract_query

## Define Inventory class
class Inventory():
    def __init__(self, key: int = None, name: str = '', quantity: int = 0, note: str = '', exists: bool = True):
        self.sql_conn = SQLService()
        self.key = key # Primary key from DB
        self.name = name
        self.quantity = quantity
        self.note = note
        self.exists = exists
        self._update_callbacks = []
        self._delete_callbacks = []
    
    def add_update_callback(self, func):
        self._update_callbacks.append(func)
    
    def add_delete_callback(self, func):
        self._delete_callbacks.append(func)
    
    def _notify_update(self):
        for cb in self._update_callbacks:
            cb()
    
    def _notify_delete(self):
        for cb in self._delete_callbacks:
            cb()
    
    def update_item(self, quantity):
        # Convert quantity to int
        try:
            quantity = int(quantity)
        except ValueError as m:
            raise ValueError(m)

        # Update instance variables
        self.quantity = quantity

        # Update the database
        if self.quantity > 0:
            self._notify_update()
            self._update_item_db()
        else:
            self._notify_delete()
            self.delete_item()
    
    def _update_item_db(self):
        if self.exists == False:
            self.insert_item_db()
            return 
    
        query = extract_query('uspUpdateInventoryItem')
        
        # Replace placeholders        
        query = query.replace('@primarykey', str(self.key))
        query = query.replace('@quantity', str(self.quantity))
        if self.note != None and self.note.strip() != '':
            query = query.replace('@note', str(self.note))
        else:
            query = query.replace("'@note'", 'NULL')

        # Update DB
        self.sql_conn.execute_update(query)
    
    def delete_item(self):
        query = extract_query('uspDeleteInventoryItem')
        
        # Replace pk placeholder with key and execute query
        query = query.replace("@primarykey", str(self.key))
        self.sql_conn.execute_update(query)

        # Update exists flag
        self.exists = False
        self._notify_delete()
    
    def insert_item_db(self):
        if self.exists == True: # Prevents insertion of existing items
            return 

        query = extract_query('uspInsertInventoryItem')
        
        # Sanitise query 
        name = self.name.replace("'","''")
        note = self.note.replace("'","''")

        # Insert into database
        query = query.replace('@name', name)
        query = query.replace('@quantity', str(self.quantity))
        query = query.replace('@description', note)

        self.key = self.sql_conn.execute_insert(query, 1)

        # Update exists flag
        self.exists = True 
        self._notify_update()
