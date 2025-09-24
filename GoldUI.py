# Define libraries
import tkinter as tk
from tkinter import messagebox
from config import *

class GoldUI():
    def __init__(self, root = None):
        self.root = root
        self.logicCB = lambda *args, **kwargs: None
    
    def UpdateGold(self, amount):
        self.goldLabel.config(text = f'Gold: {amount:,}')
    
    def PlaceWidgets(self, widgetRow):
        # Create widgets
        self.goldLabel = tk.Label(self.root)
        self.goldEntry = tk.Entry(self.root)
        self.goldButton = tk.Button(self.root, text = 'Update Gold', command = self.UpdateGoldCommand)

        # Place widgets
        self.goldLabel.grid(row = widgetRow, column = 0, padx = 5, pady = 5)
        self.goldEntry.grid(row = widgetRow, column = 1)
        self.goldButton.grid(row = widgetRow + 1, column = 1, padx = 5)

        # Update the label
        self.UpdateGold(0)
    
    def UpdateMaster(self, root):
        self.root = root
    
    def AddLogicCB(self, func):
        self.logicCB = func 
    
    def _NotifyLogicCB(self):
        self.logicCB(self.goldEntry.get())

    def UpdateGoldCommand(self):
        try:
            self._NotifyLogicCB()
            self.goldEntry.delete(0, tk.END) 
        except ValueError as m:
            messagebox.showerror('Error', f'An error occurred: {m}')