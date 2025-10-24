# Import libraries
import tkinter as tk
from tkinter import messagebox

class SpellTrackerWindow():
    def __init__(self, root):
        self.root = root 
        self.window = tk.Toplevel(self.root)
        self.window.title('Spell Tracker')
        self.window.geometry("800x600")
        self.max_characters = 20
    
    def initialise_window(self):
        self.create_ui_frames()
        self.create_new_char_widgets()
    
    def create_ui_frames(self):
        # Create frames
        self.character_frame = tk.Frame(self.window)
        self.character_detail_frame = tk.Frame(self.window)
        self.new_character_frame = tk.Frame(self.window)

        # Place frames
        self.character_frame.grid(column = 1)
        self.character_detail_frame.grid(column = 2)
        self.new_character_frame.grid(column = 3)
    
    def create_new_char_widgets(self):
        # Create widgets
        self.new_character_name_entry = tk.Entry(self.new_character_frame)
        self.new_character_button = tk.Button(self.new_character_frame, text = 'Add Character')
        self.new_character_label = tk.Label(self.new_character_frame, text = 'Character Name:')

        # Add widgets
        self.new_character_label.grid(column = 1, row = 1, padx = 5)
        self.new_character_name_entry.grid(column = 2, row = 1)
        self.new_character_button.grid(column = 2, row = 2, pady = 5)