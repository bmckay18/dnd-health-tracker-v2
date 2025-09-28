# Define libraries
from sql_service import SQLService
from functions.extract_query import extract_query

class RoundTracker():
    def __init__(self):
        self.conn = SQLService()
        self.current_round = self._retrieve_round()
    
    def _retrieve_round(self):
        query = extract_query("uspRetrieveRound")
        try:
            return int(self.conn.execute_select(query))
        except ValueError as m:
            print(m)
            return -1
    
    def next_round(self):
        try:
            self.current_round += 1
            self._update_round()
        except Exception as m:
            print(m)
    
    def _update_round(self):
        query = extract_query('uspUpdateRound') % self.current_round
        self.conn.execute_update(query)