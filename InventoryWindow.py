# Define libraries
import tkinter as tk
from tkinter import messagebox
from config import *
from inventory import Inventory
from inventoryUI import InventoryUI
import math as m

class InventoryWindow():
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.geometry("648x374")
        self.window.title("Player Inventory")
        self.page = 0
        self.maxPage = 0
        self.itemUIs = []
        self.padx = 2.5
        self.pady = 2.5
        self.displayedItemsLimit = 10 # Number of items to display per page
        self.newInventoryCallback = lambda *args, **kwargs: None
    
    def CreateUIInstances(self, items: list[Inventory]):
        for item in items:
            self.itemUIs.append(InventoryUI(self.itemFrame, item))
            
        self.SetMaxPageLimit()
    
    def SetMaxPageLimit(self):
        self.maxPage = m.ceil(len(self.itemUIs) / self.displayedItemsLimit)
    
    def CreateModalFrames(self):
        self.itemFrame = tk.Frame(self.window)
        self.editFrame = tk.Frame(self.window) 

        # Create edit frame widgets
        self.itemNameEntry = tk.Entry(self.editFrame)
        self.itemNameLabel = tk.Label(self.editFrame, text = 'Name:')

        self.itemQuantityEntry = tk.Entry(self.editFrame)
        self.itemQuantityLabel = tk.Label(self.editFrame, text = 'Quantity:')

        self.createItemButton = tk.Button(self.editFrame, text = 'Add', command = self._InsertInventoryItem)

        self.nextPageButton = tk.Button(self.editFrame, text = '>', command = self.NextPage)
        self.prevPageButton = tk.Button(self.editFrame, text = '<', command = self.PreviousPage)
        self.pageLabel = tk.Label(self.editFrame, text = f'Page: {self.page + 1}')
        self.updateQuantitiesButton = tk.Button(self.editFrame, text = 'Update Items', command = self._UpdateQuantities)

        # Place frames
        self.itemFrame.pack(side='left', fill='both', expand=True)
        self.editFrame.pack(side='left', fill='y')

        # Place edit frame widgets
        self.itemNameLabel.grid(row = 1, column = 1, padx = self.padx, pady = self.pady)
        self.itemNameEntry.grid(row = 1, column = 2, padx = self.padx, pady = self.pady)

        self.itemQuantityLabel.grid(row = 2, column = 1, padx = self.padx, pady = self.pady)
        self.itemQuantityEntry.grid(row = 2, column = 2, padx = self.padx, pady = self.pady)

        self.createItemButton.grid(row = 3, column = 2, pady = self.pady, padx = self.padx)

        self.updateQuantitiesButton.grid(row = 4, column = 2, pady = self.pady)

        self.prevPageButton.grid(row = 5, column = 1)
        self.pageLabel.grid(row = 5, column = 2, pady = self.pady * 2)
        self.nextPageButton.grid(row = 5, column = 3, padx = self.padx * 2)

    def _UpdateQuantities(self):
        for item in self.itemUIs:
            item.UpdateDatabase()
    
    def PlaceItemWidgets(self):
        page_factor = self.page * self.displayedItemsLimit

        self.pageLabel['text'] = f'Page: {self.page + 1}'

        for ui in self.itemUIs:
            ui.HideWidgets()

        try:
            for i in range(0,self.displayedItemsLimit):
                self.itemUIs[i + page_factor].DisplayWidgets(i)
        except IndexError as m:
            print(m)
    
    def InitialiseWindow(self, items: Inventory):
        self.CreateModalFrames()
        self.CreateUIInstances(items)
        self.PlaceItemWidgets()
    
    def PreviousPage(self):
        if self.page > 0:
            self.page -= 1
            self.PlaceItemWidgets()
    
    def NextPage(self):
        if self.page + 1 != self.maxPage:
            self.page += 1
            self.PlaceItemWidgets()
    
    def _InsertInventoryItem(self):
        name = self.itemNameEntry.get()
        try:
            quantity = int(self.itemQuantityEntry.get())
            self.newInventoryCallback(name, quantity)
            self.PlaceItemWidgets()
        except ValueError as m:
            messagebox.showerror("Error", f'An error occurred: {m}')
        finally:
            self.itemNameEntry.delete(0, tk.END)
            self.itemQuantityEntry.delete(0, tk.END)
    
    def AddInsertInventoryCallback(self, func):
        self.newInventoryCallback = func