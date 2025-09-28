# Define libraries
import tkinter as tk

class RoundUI():
    def __init__(self, master):
        self.master = master

        # Initialise cb functions
        self.next_round_cb = lambda *args, **kwargs: None
        self.prev_round_cb = lambda *args, **kwargs: None
        self.reset_rounds_cb = lambda *args, **kwargs: None

        # Initialise widgets
        self.create_widgets()

    def create_widgets(self):
        self.round_label = tk.Label(self.master)
        self._update_label(0)
        self.next_round_button = tk.Button(self.master, text = 'Next Round', command = None)
        self.prev_round_button = tk.Button(self.master, text = 'Previous Round / Reset', command = None)
    
    def place_widgets(self, set_row: int):
        self.round_label.grid(row = set_row, column = 0)
        self.next_round_button.grid(row = set_row + 1, column = 0)
        self.prev_round_button.grid(row = set_row + 2, column = 0)
    
    def _update_label(self, current_round):
        self.round_label.config(text = f'Round: {current_round}')
    
    def add_callback_functions(self, next_cb, prev_cb, reset_cb):
        self.next_round_cb = next_cb
        self.prev_round_cb = prev_cb
        self.reset_rounds_cb = reset_cb

        # Update button widgets
        self.next_round_button.config(command = self.next_round_cb)
        self.prev_round_button.config(command = self.prev_round_cb)
        self.prev_round_button.bind("<Button-3>", self.reset_rounds_cb)