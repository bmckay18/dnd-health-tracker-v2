# Define libraries
from sql_service import SQLService
from functions.extract_query import extract_query

class RoundTracker():
    def __init__(self):
        self.conn = SQLService()
        self.current_round = 0
        self.ui_cb = lambda *args, **kwargs: None
        self._retrieve_round()
    
    def _retrieve_round(self):
        query = extract_query("uspRetrieveRound")
        try:
            current_round = self.conn.execute_select(query)[0][0]
            self.current_round = current_round
        except ValueError as m:
            print(m)
    
    def _notify_ui_cb(self):
        self.ui_cb(self.current_round)
    
    def add_ui_cb(self, func):
        self.ui_cb = func
    
    def next_round(self):
        try:
            self.current_round += 1
            self._notify_ui_cb()
            self._update_round()
        except Exception as m:
            print(m)
    
    def prev_round(self):
        try:
            self.current_round = max(self.current_round - 1, 0) # Ensures that the minimum round number is 0
            self._notify_ui_cb()
            self._update_round()
        except Exception as m:
            print(m)
    
    def _update_round(self):
        query = extract_query('uspUpdateRound') % self.current_round
        self.conn.execute_update(query)