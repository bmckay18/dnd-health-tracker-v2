# Define libraries
from sqlService import SQLService
from config import *
from functions.ExtractQuery import ExtractQuery

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
    
    def UpdateItem(self, quantity):
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
            self._UpdateItemDB()
        else:
            self._notify_delete()
            self.DeleteItem()
    
    def _UpdateItemDB(self):
        if self.exists == False:
            self.InsertItemDB()
            return 
    
        query = ExtractQuery('uspUpdateInventoryItem')
        
        # Replace placeholders        
        query = query.replace('@primarykey', str(self.key))
        query = query.replace('@quantity', str(self.quantity))
        if self.note != None and self.note.strip() != '':
            query = query.replace('@note', str(self.note))
        else:
            query = query.replace("'@note'", 'NULL')

        # Update DB
        self.sql_conn.ExecuteUpdate(query)
    
    def DeleteItem(self):
        query = ExtractQuery('uspDeleteInventoryItem')
        
        # Replace pk placeholder with key and execute query
        query = query.replace("@primarykey", str(self.key))
        self.sql_conn.ExecuteUpdate(query)

        # Update exists flag
        self.exists = False
        self._notify_delete()
    
    def InsertItemDB(self):
        if self.exists == True: # Prevents insertion of existing items
            return 

        query = ExtractQuery('uspInsertInventoryItem')
        
        # Sanitise query 
        name = self.name.replace("'","''")
        note = self.note.replace("'","''")

        # Insert into database
        query = query.replace('@name', name)
        query = query.replace('@quantity', str(self.quantity))
        query = query.replace('@description', note)

        self.key = self.sql_conn.ExecuteInsert(query, 1)

        # Update exists flag
        self.exists = True 
        self._notify_update()
