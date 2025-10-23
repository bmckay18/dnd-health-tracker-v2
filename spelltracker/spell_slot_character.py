# Import libraries
from spelltracker import SpellSlot

class SpellSlotCharacter():
    def __init__(self, character_id, name):
        self.character_id = character_id
        self.name = name
        self.spell_slots = []
    
    def add_spell_slot(self, spell_slot: SpellSlot):
        self.spell_slots.append(spell_slot)
    
    def regain_spent_spell_slots(self):
        for spell in self.spell_slots:
            spell.reset_spell_slot()
    
    def expend_spell_slot(self, spell_level):
        for spell in self.spell_slots:
            if spell.spell_slot_level == spell_level:
                spell.use_spell_slot()
                break
    
    def regain_spell_slot(self, spell_level):
        for spell in self.spell_slots:
            if spell.spell_slot_level == spell_level:
                spell.regain_spell_slot()
                break
    