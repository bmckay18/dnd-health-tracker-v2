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
        self.name_label = tk.Label(self.root, text = self.item.name)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.insert(0, str(self.item.quantity))
        self.note_button = tk.Button(self.root, text = 'Description', command = self.create_note_modal)
    
    def create_note_modal(self):
        # Create window
        self.note_modal_window = tk.Toplevel(self.root)
        self.note_modal_window.title("Item Note")
        self.note_modal_window.lift()
        self.note_modal_window.focus_force()

        # Create widgets
        self.note_text = tk.Text(self.note_modal_window, width = 80, height = 5)
        self.note_save_button = tk.Button(self.note_modal_window, text = 'Update Note', command = self._update_note)

        # Place widgets
        self.note_text.grid(row = 1, column = 1, pady = 5, padx = 5)
        self.note_save_button.grid(row = 2, column = 1, pady = 5)

        # Update text
        self.note_text.insert("1.0", self.item.note)
    
    def _update_note(self):
        self.item.note = self.note_text.get("1.0", tk.END)
        self.note_modal_window.destroy()
    
    def display_widgets(self, ui_row):
        y_pad = 5
        x_pad = 2.5

        # Display widgets
        self.name_label.grid(row = ui_row, column = 1, pady = y_pad, padx = x_pad)
        self.quantity_entry.grid(row = ui_row, column = 2, pady = y_pad, padx = x_pad)
        self.note_button.grid(row = ui_row, column = 3, pady = y_pad, padx = x_pad)
    
    def hide_widgets(self):
        self.name_label.grid_forget()
        self.quantity_entry.grid_forget()
        self.note_button.grid_forget()
    
    def update_database(self):
        self.item.update_item(self.quantity_entry.get())
    
    def _notify_delete(self):
        for func in self._callback:
            func()
    
    def _add_cb(self, func):
        self._callback.append(func)