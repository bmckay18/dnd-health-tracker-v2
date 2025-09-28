# Define libraries
from sql_service import SQLService
from functions.extract_query import extract_query

class RoundTracker():
    def __init__(self):
        self.conn = SQLService()
        self.round = self._retrieve_round()
    
    def _retrieve_round(self):
        query = extract_query("uspRetrieveRound")
        try:
            return int(self.conn.execute_select(query))
        except ValueError as m:
            print(m)
            return -1