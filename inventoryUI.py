# Define libraries
import tkinter as tk
from config import *
from inventory import Inventory

class InventoryUI():
    def __init__(self, root, inventory: Inventory):
        self.root = root
        self.item = inventory
        self.create_ui_widgets()
        self._callback = []
    
    def create_ui_widgets(self):
        # Create widgets
        self.nameLabel = tk.Label(self.root, text = self.item.name)
        self.quantityEntry = tk.Entry(self.root)
        self.quantityEntry.insert(0, str(self.item.quantity))
        self.noteButton = tk.Button(self.root, text = 'Description', command = self.create_note_modal)
    
    def create_note_modal(self):
        # Create window
        self.noteModalWindow = tk.Toplevel(self.root)
        self.noteModalWindow.title("Item Note")
        self.noteModalWindow.lift()
        self.noteModalWindow.focus_force()

        # Create widgets
        self.noteText = tk.Text(self.noteModalWindow, width = 80, height = 5)
        self.noteSaveButton = tk.Button(self.noteModalWindow, text = 'Update Note', command = self._update_note)

        # Place widgets
        self.noteText.grid(row = 1, column = 1, pady = 5, padx = 5)
        self.noteSaveButton.grid(row = 2, column = 1, pady = 5)

        # Update text
        self.noteText.insert("1.0", self.item.note)
    
    def _update_note(self):
        self.item.note = self.noteText.get("1.0", tk.END)
        self.noteModalWindow.destroy()
    
    def display_widgets(self, UIrow):
        y_pad = 5
        x_pad = 2.5

        # Display widgets
        self.nameLabel.grid(row = UIrow, column = 1, pady = y_pad, padx = x_pad)
        self.quantityEntry.grid(row = UIrow, column = 2, pady = y_pad, padx = x_pad)
        self.noteButton.grid(row = UIrow, column = 3, pady = y_pad, padx = x_pad)
    
    def hide_widgets(self):
        self.nameLabel.grid_forget()
        self.quantityEntry.grid_forget()
        self.noteButton.grid_forget()
    
    def update_database(self):
        self.item.UpdateItem(self.quantityEntry.get())
    
    def _notify_delete(self):
        for func in self._callback:
            func()
    
    def _add_cb(self, func):
        self._callback.append(func)