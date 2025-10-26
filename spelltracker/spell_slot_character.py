# Import libraries
from spelltracker import SpellSlot
from sql_service import SQLService

class SpellSlotCharacter():
    def __init__(self, character_id, name):
        self.character_id = character_id
        self.name = name
        self.spell_slots = []
        self.conn = SQLService()
    
    def add_spell_slot(self, spell_slot: SpellSlot): # Need to implement method for retrieving data from DB
        self.spell_slots.append(spell_slot)
    
    def regain_spent_spell_slots(self):
        for spell in self.spell_slots:
            spell.reset_spell_slot()
        self.update_db()
    
    def set_remaining_spell_slot(self, spell_level, remaining_slots):
        for spell in self.spell_slots:
            if spell_level == spell.spell_slot_level:
                spell.set_spell_slot(remaining_slots)
        self.update_db()
    
    def update_db(self):
        base_query = 'UPDATE tblSpellAttributes'
        for spell in self.spell_slots:
            query = base_query
            query += f' {spell.generate_db_string()}'
            query += f' WHERE colSpellAttributesCharacterID = {self.character_id}'
            query += f' AND colSpellAttributesSpellSlot = {spell.spell_slot_level}'
            self.conn.execute_update(query)