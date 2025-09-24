# Define libraries
import tkinter as tk
from config import *
from inventory import Inventory

class InventoryUI():
    def __init__(self, root, inventory: Inventory):
        self.root = root
        self.item = inventory
        self.CreateUIWidgets()
        self._callback = []
    
    def CreateUIWidgets(self):
        # Create widgets
        self.nameLabel = tk.Label(self.root, text = self.item.name)
        self.quantityEntry = tk.Entry(self.root)
        self.quantityEntry.insert(0, str(self.item.quantity))
        self.noteButton = tk.Button(self.root, text = 'Description', command = self.CreateNoteModal)
    
    def CreateNoteModal(self):
        # Create window
        self.noteModalWindow = tk.Toplevel(self.root)
        self.noteModalWindow.title("Item Note")
        self.noteModalWindow.lift()
        self.noteModalWindow.focus_force()

        # Create widgets
        self.noteText = tk.Text(self.noteModalWindow, width = 80, height = 5)
        self.noteSaveButton = tk.Button(self.noteModalWindow, text = 'Update Note', command = self._UpdateNote)

        # Place widgets
        self.noteText.grid(row = 1, column = 1, pady = 5, padx = 5)
        self.noteSaveButton.grid(row = 2, column = 1, pady = 5)

        # Update text
        self.noteText.insert("1.0", self.item.note)
    
    def _UpdateNote(self):
        self.item.note = self.noteText.get("1.0", tk.END)
        self.noteModalWindow.destroy()
    
    def DisplayWidgets(self, UIrow):
        y_pad = 5
        x_pad = 2.5

        # Display widgets
        self.nameLabel.grid(row = UIrow, column = 1, pady = y_pad, padx = x_pad)
        self.quantityEntry.grid(row = UIrow, column = 2, pady = y_pad, padx = x_pad)
        self.noteButton.grid(row = UIrow, column = 3, pady = y_pad, padx = x_pad)
    
    def HideWidgets(self):
        self.nameLabel.grid_forget()
        self.quantityEntry.grid_forget()
        self.noteButton.grid_forget()
    
    def UpdateDatabase(self):
        self.item.UpdateItem(self.quantityEntry.get())
    
    def _Notify_Delete(self):
        for func in self._callback:
            func()
    
    def _AddCallback(self, func):
        self._callback.append(func)