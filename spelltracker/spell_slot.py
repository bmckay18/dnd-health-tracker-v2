# Import libraries

class SpellSlot():
    def __init__(self, spell_slot_level, spell_slot_max, spell_slot_current):
        self.spell_slot_level = spell_slot_level
        self.spell_slot_max = spell_slot_max
        self.spell_slot_current = spell_slot_current
    
    def reset_spell_slots(self):
        self.spell_slot_current = self.spell_slot_max
    
    def use_spell_slot(self):
        self.spell_slot_current -= 1
        if self.spell_slot_current < 0:
            self.spell_slot_current = 0
    
    def regain_spell_slot(self):
        self.spell_slot_current += 1
        if self.spell_slot_current > self.spell_slot_max:
            self.spell_slot_current = self.spell_slot_max
    
    
