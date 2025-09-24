# Define libraries
from sqlService import SQLService
from config import *
from functions.ExtractQuery import extract_query

class GoldService():
    def __init__(self):
        self.conn = SQLService()
        self.amount = self._retrieve_amount()
        self.UICallback = lambda *args, **kwargs: None 
    
    def _retrieve_amount(self):
        query = extract_query('uspSelectGoldAmount')
        
        return self.conn.execute_select(query)[0][0]

    def _update_amount(self, difference):
        query = extract_query('uspUpdateGoldAmount')
        
        query = query.replace("@amount", str(self.amount))
        query = query.replace("@difference", str(difference))

        self.conn.execute_update(query)
    
    def get_amount(self):
        return self.amount
    
    def update_amount(self, difference):
        try:
            difference = int(difference)
        except ValueError as m:
            raise ValueError(m)
        
        self.amount += difference 
        self._update_amount(difference)
        self._notify_cb()
    
    def _notify_cb(self):
        self.UICallback(self.get_amount())
    
    def add_cb(self, func):
        self.UICallback = func