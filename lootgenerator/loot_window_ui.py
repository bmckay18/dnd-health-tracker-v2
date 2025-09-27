# Define libraries
import tkinter as tk

class LootWindowUI():
    def __init__(self, master, items):
        self.master = master 
        self.items = items
        self.window = tk.Toplevel(self.master)
        self.fixed_width = 350
        self.window.transient(self.master)
        self._setup()
    
    def _setup(self):
        self.window.title('Generated Items')
        tk.Label(self.window, text = 'Generated Items:').grid(row = 0, column = 0, pady = 0, padx = 5)
        self.window.geometry(f"{self.fixed_width}x100")
        self._display_items()
    
    def _display_items(self):
        c_row = 0
        y_pad = 0
        for item in self.items:
            c_row += 1
            tk.Label(self.window, text = item).grid(row = c_row, column = 0, pady = y_pad, padx = 5)
        
        self.window.update_idletasks()
        needed_height = self.window.winfo_reqheight() + 10
        self.window.geometry(f"{self.fixed_width}x{needed_height}")