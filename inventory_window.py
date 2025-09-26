# Define libraries
import tkinter as tk
from tkinter import messagebox
from config import *
from inventory import Inventory
from inventory_ui import InventoryUI
import math as m

class InventoryWindow():
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.geometry("648x374")
        self.window.title("Player Inventory")
        self.page = 0
        self.max_page = 0
        self.item_uis = []
        self.padx = 2.5
        self.pady = 2.5
        self.displayed_items_limit = 10 # Number of items to display per page
        self.new_inventory_cb = lambda *args, **kwargs: None
    
    def create_ui_instances(self, items: list[Inventory]):
        for item in items:
            self.item_uis.append(InventoryUI(self.item_frame, item))
            
        self.set_max_page_limit()
    
    def set_max_page_limit(self):
        self.max_page = m.ceil(len(self.item_uis) / self.displayed_items_limit)
    
    def create_modal_frames(self):
        self.item_frame = tk.Frame(self.window)
        self.edit_frame = tk.Frame(self.window) 

        # Create edit frame widgets
        self.item_name_entry = tk.Entry(self.edit_frame)
        self.item_name_label = tk.Label(self.edit_frame, text = 'Name:')

        self.item_quantity_entry = tk.Entry(self.edit_frame)
        self.item_quantity_label = tk.Label(self.edit_frame, text = 'Quantity:')

        self.create_item_button = tk.Button(self.edit_frame, text = 'Add', command = self._insert_inventory_item)

        self.next_page_button = tk.Button(self.edit_frame, text = '>', command = self.next_page)
        self.prev_page_button = tk.Button(self.edit_frame, text = '<', command = self.previous_page)
        self.page_label = tk.Label(self.edit_frame, text = f'Page: {self.page + 1}')
        self.update_quantities_button = tk.Button(self.edit_frame, text = 'Update Items', command = self._update_quantities)

        # Place frames
        self.item_frame.pack(side='left', fill='both', expand=True)
        self.edit_frame.pack(side='left', fill='y')

        # Place edit frame widgets
        self.item_name_label.grid(row = 1, column = 1, padx = self.padx, pady = self.pady)
        self.item_name_entry.grid(row = 1, column = 2, padx = self.padx, pady = self.pady)

        self.item_quantity_label.grid(row = 2, column = 1, padx = self.padx, pady = self.pady)
        self.item_quantity_entry.grid(row = 2, column = 2, padx = self.padx, pady = self.pady)

        self.create_item_button.grid(row = 3, column = 2, pady = self.pady, padx = self.padx)

        self.update_quantities_button.grid(row = 4, column = 2, pady = self.pady)

        self.prev_page_button.grid(row = 5, column = 1)
        self.page_label.grid(row = 5, column = 2, pady = self.pady * 2)
        self.next_page_button.grid(row = 5, column = 3, padx = self.padx * 2)

    def _update_quantities(self):
        for item in self.item_uis:
            item.update_database()
    
    def place_item_widgets(self):
        page_factor = self.page * self.displayed_items_limit

        self.page_label['text'] = f'Page: {self.page + 1}'

        for ui in self.item_uis:
            ui.hide_widgets()

        try:
            for i in range(0,self.displayed_items_limit):
                self.item_uis[i + page_factor].display_widgets(i)
        except IndexError as m:
            print(m)
    
    def init_window(self, items: Inventory):
        self.create_modal_frames()
        self.create_ui_instances(items)
        self.place_item_widgets()
    
    def previous_page(self):
        if self.page > 0:
            self.page -= 1
            self.place_item_widgets()
    
    def next_page(self):
        if self.page + 1 != self.max_page:
            self.page += 1
            self.place_item_widgets()
    
    def _insert_inventory_item(self):
        name = self.item_name_entry.get()
        try:
            quantity = int(self.item_quantity_entry.get())
            self.new_inventory_cb(name, quantity)
            self.place_item_widgets()
        except ValueError as m:
            messagebox.showerror("Error", f'An error occurred: {m}')
        finally:
            self.item_name_entry.delete(0, tk.END)
            self.item_quantity_entry.delete(0, tk.END)
    
    def add_insert_inventory_callback(self, func):
        self.new_inventory_cb = func