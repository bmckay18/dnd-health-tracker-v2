# Define libraries
from sqlService import SQLService
from config import *
from functions.ExtractQuery import extract_query

class GoldService():
    def __init__(self):
        self.conn = SQLService()
        self.amount = self._RetrieveAmount()
        self.UICallback = lambda *args, **kwargs: None 
    
    def _RetrieveAmount(self):
        query = extract_query('uspSelectGoldAmount')
        
        return self.conn.ExecuteSelect(query)[0][0]

    def _UpdateAmount(self, difference):
        query = extract_query('uspUpdateGoldAmount')
        
        query = query.replace("@amount", str(self.amount))
        query = query.replace("@difference", str(difference))

        self.conn.execute_update(query)
    
    def GetAmount(self):
        return self.amount
    
    def UpdateAmount(self, difference):
        try:
            difference = int(difference)
        except ValueError as m:
            raise ValueError(m)
        
        self.amount += difference 
        self._UpdateAmount(difference)
        self._NotifyCB()
    
    def _NotifyCB(self):
        self.UICallback(self.GetAmount())
    
    def AddCB(self, func):
        self.UICallback = func