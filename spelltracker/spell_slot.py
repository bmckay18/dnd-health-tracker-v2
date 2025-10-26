# Import libraries

class SpellSlot():
    def __init__(self, spell_slot_level, spell_slot_max, spell_slot_current):
        self.spell_slot_level = spell_slot_level
        self.spell_slot_max = spell_slot_max
        self.spell_slot_current = spell_slot_current
    
    def reset_spell_slot(self):
        self.spell_slot_current = self.spell_slot_max
    
    def set_spell_slot(self, new_current):
        if (new_current <= self.spell_slot_max) & (new_current >= 0):
            self.spell_slot_current = new_current
        elif new_current > self.spell_slot_max:
            self.spell_slot_current = self.spell_slot_max
        else:
            raise ValueError('Remaining spell slots cannot be negative')
    
    def set_max_spell_slots(self, max_spells):
        if max_spells > 0:
            self.spell_slot_max = max_spells
        else:
            self.spell_slot_max = 0

        self.reset_spell_slot()        

    def generate_db_string(self):
        query = f'SET colSpellAttributesSpellSlotMax = {self.spell_slot_max}, '
        query += f'colSpellAttributesSpellSlotCurrent = {self.spell_slot_current}'
        return query