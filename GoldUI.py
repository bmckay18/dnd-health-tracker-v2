# Define libraries
import tkinter as tk
from tkinter import messagebox
from config import *

class GoldUI():
    def __init__(self, root = None):
        self.root = root
        self.logicCB = lambda *args, **kwargs: None
    
    def update_gold(self, amount):
        self.goldLabel.config(text = f'Gold: {amount:,}')
    
    def place_widgets(self, widgetRow):
        # Create widgets
        self.goldLabel = tk.Label(self.root)
        self.goldEntry = tk.Entry(self.root)
        self.goldButton = tk.Button(self.root, text = 'Update Gold', command = self.update_gold_cmd)

        # Place widgets
        self.goldLabel.grid(row = widgetRow, column = 0, padx = 5, pady = 5)
        self.goldEntry.grid(row = widgetRow, column = 1)
        self.goldButton.grid(row = widgetRow + 1, column = 1, padx = 5)

        # Update the label
        self.update_gold(0)
    
    def update_master(self, root):
        self.root = root
    
    def add_logic_cb(self, func):
        self.logicCB = func 
    
    def _notify_logic_cb(self):
        self.logicCB(self.goldEntry.get())

    def update_gold_cmd(self):
        try:
            self._notify_logic_cb()
            self.goldEntry.delete(0, tk.END) 
        except ValueError as m:
            messagebox.showerror('Error', f'An error occurred: {m}')