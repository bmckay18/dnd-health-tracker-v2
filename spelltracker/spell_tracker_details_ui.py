# Import libraries
import tkinter as tk
from spell_slot_character import SpellSlotCharacter
from details_ui_spell_widgets import DetailsUISpellWidgets

class SpellTrackerDetailsUI():
    def __init__(self, root, character_logic: SpellSlotCharacter):
        self.root = root
        self.character_logic = character_logic
        self.spell_uis = []
    
    def create_spell_uis(self):
        for spell in self.character_logic.spell_slots:
            self.spell_uis.append(DetailsUISpellWidgets(spell, self.root))
    
    def create_widgets(self):
        # Create widgets
        self.character_label = tk.Label(self.root, text = self.character_logic.name)
        self.reset_spells_buttons = tk.Button(self.root, text = 'Long Rest', command = None)
        self.create_spell_uis()

        # Place widgets
        widget_row = 1
        padding = 5

        self.character_label.grid(row = 0, column = 0, pady = padding, padx = padding)

        for spell_ui in self.spell_uis:
            spell_ui.create_and_place_widgets(widget_row)
            widget_row += 1
        
        self.reset_spells_buttons.grid(row = widget_row, column = 1, pady = padding)