# Import libraries
import tkinter as tk 
from spell_slot import SpellSlot

class DetailsUISpellWidget():
    def __init__(self, spell_instance: SpellSlot, root):
        self.root = root 
        self.spell_info = spell_instance
        self.frame = tk.Frame(root)
    
    def create_and_place_widgets(self, widget_row):
        raise NotImplementedError('This has not been implemented')