# Define libraries
from config import *
import tkinter as tk
from tkinter import ttk

# The LootUI class will handle the UI integration into the health tracker UI
# It will then make a callback to both the LootGen class and the LootWindowUI class
# to generate the loot and display these results in a new window

class LootUI():
    def __init__(self, master, options: list[str]):
        self.root = master
        self.options = options
        self.combo_selected = None
        self.combo_box = None 
        self.amount_entry = None 
        self.gen_button = None 
    
    def place_widgets(self, row):
        # Create combo menu widget
        self.combo_selected = tk.StringVar(self.root)
        self.combo_box = ttk.Combobox(self.root, textvariable=self.combo_selected,
                                      values = self.options, state = 'readonly',
                                      width = 5)
        self.combo_box.current(0)

        # Create amount entry widget
        self.amount_entry = tk.Entry(self.root)

        # Create button to generate loot
        self.gen_button = tk.Button(self.root, text = 'Generate Loot', command = None)

        # Pack widgets into UI window
        self.combo_box.grid(row = row, column = 0, pady = 5)
        self.amount_entry.grid(row = row, column = 1, padx = 5)
        self.gen_button.grid(row = row + 1, column = 1, pady = 5)