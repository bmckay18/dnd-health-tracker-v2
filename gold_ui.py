# Define libraries
import tkinter as tk
from tkinter import messagebox
from config import *

class GoldUI():
    def __init__(self, root = None):
        self.root = root
        self.logic_cb = lambda *args, **kwargs: None
    
    def update_gold(self, amount):
        self.gold_label.config(text = f'Gold: {amount:,}')
    
    def place_widgets(self, widget_row):
        # Create widgets
        self.gold_label = tk.Label(self.root)
        self.gold_entry = tk.Entry(self.root)
        self.gold_button = tk.Button(self.root, text = 'Update Gold', command = self.update_gold_cmd)

        # Place widgets
        self.gold_label.grid(row = widget_row, column = 0, padx = 5, pady = 5)
        self.gold_entry.grid(row = widget_row, column = 1)
        self.gold_button.grid(row = widget_row + 1, column = 1, padx = 5)

        # Update the label
        self.update_gold(0)
    
    def update_master(self, root):
        self.root = root
    
    def add_logic_cb(self, func):
        self.logic_cb = func 
    
    def _notify_logic_cb(self):
        self.logic_cb(self.gold_entry.get())

    def update_gold_cmd(self):
        try:
            self._notify_logic_cb()
            self.gold_entry.delete(0, tk.END) 
        except ValueError as m:
            messagebox.showerror('Error', f'An error occurred: {m}')