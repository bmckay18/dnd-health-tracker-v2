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
        self.initialise_window()
    
    def initialise_window(self):
        self.create_ui_frames()
    
    def create_ui_frames(self):
        self.character_frame = tk.Frame(self.window)
        self.character_detail_frame = tk.Frame(self.window)
        self.new_character_frame = tk.Frame(self.window)