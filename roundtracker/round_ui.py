# Define libraries
import tkinter as tk

class RoundUI():
    def __init__(self, master = None):
        self.master = master
        
        # Initialise tk widgets
        self.round_label = None 
        self.next_round_button = None 
        self.prev_round_button = None

        # Initialise cb functions
        self.next_round_cb = lambda *args, **kwargs: None
        self.prev_round_cb = lambda *args, **kwargs: None

    def place_widgets(self, set_row: int):
        # Create widgets
        self.round_label = tk.Label(self.master, text = 'Round: ')
        self.next_round_button = tk.Button(self.master, text = 'Next Round', command = self.next_round_cb)
        self.prev_round_button = tk.Button(self.master, text = 'Previous Round', command = self.prev_round_cb)

        # Place widgets
        self.round_label.grid(row = set_row, column = 0)
        self.next_round_button.grid(row = set_row + 1, column = 0)
        self.prev_round_button.grid(row = set_row + 2, column = 0)
    
    def update_label(self, current_round):
        self.round_label['text'] = f'Round: {current_round}'
    
    def add_callback_functions(self, next_cb, prev_cb):
        self.next_round_cb = next_cb
        self.prev_round_cb = prev_cb
    
    def update_master(self, master):
        self.master = master