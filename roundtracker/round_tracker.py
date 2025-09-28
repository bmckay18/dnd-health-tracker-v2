# Define libraries
from sql_service import SQLService
from functions.extract_query import extract_query

class RoundTracker():
    def __init__(self):
        self.conn = SQLService()