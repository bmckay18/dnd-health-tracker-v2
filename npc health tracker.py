# Define libraries
import tkinter as tk
from tkinter import messagebox
from sqlService import SQLService
from config import *
from InventoryWindow import InventoryWindow
from inventory import Inventory
from GoldService import GoldService
from GoldUI import GoldUI
from functions.ExtractQuery import extract_query

# Establish DB connection
sql_conn = SQLService()
sql_conn.create_db() # Creates the database if it doesn't exist

# Establish Gold service
gold = GoldService()
goldInterface = GoldUI()
gold.AddCB(goldInterface.UpdateGold)
goldInterface.AddLogicCB(gold.UpdateAmount)

# Define NPC class
class NPC():
    def __init__(self, name, hp_max=1, ac=10, master_win=None):
        self.hp_max = hp_max
        self.hp_current = hp_max
        self.ac = ac 
        self.name = name
        self.labelWidget = tk.Label(master_win, text=f'{self.name} : {self.hp_current} HP')
        self.widgetStringVar = tk.StringVar(master_win)
        self.entryWidget = tk.Entry(master_win, textvariable=self.widgetStringVar)
        self.buttonWidget = tk.Button(master_win, text='Remove') # Need to add command to this
        self.checkbool = tk.IntVar(master_win)
        self.checkwidget = tk.Checkbutton(master_win, variable=self.checkbool)
        self.isDead = False
    
    def SaveState(self):
        if self.hp_current > 0 and self.isDead == False:
            return [self.name, str(self.hp_max), str(self.hp_current)]
        else:
            return -1
    
    def ModifyHP(self, amount):
        if self.isDead == False: # Prevent dead npcs from regaining life
            self.hp_current += amount
        
        if self.hp_current > self.hp_max:
            self.hp_current = self.hp_max
        elif self.hp_current <= 0:
            self.hp_current = 0
            self.DisableNPC()
            self.isDead = True
        
        self.UpdateLabel()
        self.checkbool.set(0)
    
    def Destruct(self): # Unused
        self.buttonWidget.destroy()
        self.labelWidget.destroy()
        self.entryWidget.destroy()
        self.checkwidget.destroy()
    
    def DisableNPC(self):
        self.entryWidget['state'] = 'disabled'
        self.checkwidget['state'] = 'disabled'
        self.checkbool.set(0)

    def PackWidgets(self, position, npc_column=0):
        npc_column *= 3 # This variable controls if the widgets should be place in column 0,1,2
        self.entryWidget.grid(row=position, column=1 + npc_column, pady = 3)
        self.labelWidget.grid(row=position, column=0 + npc_column)
        self.checkwidget.grid(row=position, column = 2 + npc_column)
    
    def UpdateLabel(self):
        self.labelWidget['text'] = f'{self.name} : {self.hp_current} HP'
    
    def HealthCheck(self):
        global mass_update_var
        if self.checkbool.get() == 0:
            temp_hp = self.widgetStringVar.get()
        else:
            temp_hp = mass_update_var.get()
        
        if temp_hp == '': # Ignore if the field is empty
            return
        
        try: # Try to evaluate temp_hp to int and update hp
            temp_hp = eval(temp_hp)
            self.ModifyHP(temp_hp)
            self.widgetStringVar.set('')
        except NameError as m:
            print(m)
        except Exception as m:
            print(m)


# Define functions 
def AddNewNPC():
    global name_var, ac_var, hp_var, npc_list, root, quantity_var

    if name_var.get() == '' or hp_var.get() == '': # Validation that name and hp were entered
        print('NPC must have a name and hp value')
        return

    if quantity_var.get() == '': # Sets quantity var to 1 if left blank
        quantity_var.set('1')
    
    try:
        quantity_num = eval(quantity_var.get())
        for q in range(0, quantity_num):
            num_string = q # number to add on to npc name
            if quantity_num == 1:
                num_string = ''
            else:
                num_string = q + 1

            if len(npc_list) < 23: # Place in first column
                temp_npc = NPC(f'{name_var.get()} {num_string}', int(hp_var.get()), ac_var.get(), existing_npc_frame)
                npc_list.append(temp_npc)
                temp_npc.PackWidgets(len(npc_list)-1, 0)
            elif len(npc_list) < 46: # Place in second column
                temp_npc = NPC(f'{name_var.get()} {num_string}', int(hp_var.get()), ac_var.get(), existing_npc_frame_2)
                npc_list.append(temp_npc)
                temp_npc.PackWidgets(len(npc_list)-24, 0)
    except ValueError as vm:
        print(vm)
    except Exception as m:
        print(m)

    ClearNewFields()

def UpdateHealth():
    global npc_list, mass_update_var, allcheck_var, checkbox_selector 
    destroy_npcs = []
    for npc in npc_list:
        npc.HealthCheck()
        if npc.hp_current == 0:
            destroy_npcs.append(npc)
    
    mass_update_var.set('') # Reset mass update var

    if allcheck_var.get() == 1:
        checkbox_selector.invoke()

def ClearNewFields():
    global name_var, hp_var, quantity_var
    name_var.set('')
    hp_var.set('')
    quantity_var.set('')

def SelectCheckboxes():
    global allcheck_var, npc_list
    for npc in npc_list:
        npc.checkbool.set(allcheck_var.get())

def DeleteAllNPCs():
    global npc_list
    for npc in npc_list:
        npc.Destruct()
    
    npc_list = []

### Save Functions
def CreateSave():
    global npc_list, sql_conn

    try:
        # Retrieve insert usp
        base_query = extract_query('uspInsertNPCData')
        query = 'DELETE FROM tblNPC;\n'
        for npc in npc_list:
            saveState = npc.SaveState()
            if saveState == -1:
                continue
            else:
                temp_query = base_query.replace('@name', saveState[0])
                temp_query = temp_query.replace('@maxHP', saveState[1])
                temp_query = temp_query.replace('@currentHP', saveState[2])
                query += temp_query + '\n'
            
        sql_conn.execute_insert(query)

        # Display successful save message to user
        messagebox.showinfo('Success','NPC Data Saved')
    except Exception as m:
        print(m)
        messagebox.showerror('Failed',f'NPC data failed to saved. Error: {m}')

def LoadSave():
    global npc_list

    try:
        query = extract_query('uspSelectNPCData')
        content = sql_conn.execute_select(query)
        # Create new NPC object 
        for data_split in content:
            t_name = data_split[0]
            t_maxHP = int(data_split[1])
            t_currentHP = int(data_split[2])
            if len(npc_list) < 23: # Place in first column
                temp_npc = NPC(f'{t_name}', t_maxHP, ac_var.get(), existing_npc_frame)
                temp_npc.hp_current = t_currentHP
                temp_npc.UpdateLabel()
                npc_list.append(temp_npc)
                temp_npc.PackWidgets(len(npc_list)-1, 0)
            elif len(npc_list) < 46: # Place in second column
                temp_npc = NPC(f'{t_name}', t_maxHP, ac_var.get(), existing_npc_frame_2)
                temp_npc.hp_current = t_currentHP
                temp_npc.UpdateLabel()
                npc_list.append(temp_npc)
                temp_npc.PackWidgets(len(npc_list)-24, 0)
    except Exception as m:
        print(m)

## Inventory functions
inventory_window = None 
def OpenInventoryButton():
    global inventory_window, root
    inventory_items = sql_conn.execute_select(extract_query('uspSelectInventoryItemsAll'))

    inventory_class_objects = []
    for item in inventory_items:
        tmp_inventory = Inventory(item[0], item[1], int(item[2]), item[3])
        inventory_class_objects.append(tmp_inventory)
    
    OpenInventoryWindow(inventory_class_objects)
    
def OpenInventoryWindow(items):
    global inventory_window, root 
    inventory_window = InventoryWindow(root)
    inventory_window.AddInsertInventoryCallback(AddNewInventoryItem)
    inventory_window.InitialiseWindow(items)

def AddNewInventoryItem(itemName, itemQuantity):
    global inventory_window
    tmpInv = Inventory(name = itemName, quantity = itemQuantity, exists = False)
    inventory_window.CreateUIInstances([tmpInv])

### UI
# Initialise UI window
root = tk.Tk()
existing_npc_frame = tk.Frame(root)
existing_npc_frame_2 = tk.Frame(root)
new_npc_frame = tk.Frame(root)
root.geometry("1000x580") # Originally 1000x600
root.title("NPC Health Tracker")

# Define variables to store data in
npc_list = []

# Define new NPC widgets
name_var = tk.StringVar(new_npc_frame)
ac_var = tk.StringVar(new_npc_frame)
hp_var = tk.StringVar(new_npc_frame)
quantity_var = tk.StringVar(new_npc_frame)
allcheck_var = tk.IntVar(new_npc_frame) # Boolean for the checkbutton that controls all checkbuttons
mass_update_var = tk.StringVar(new_npc_frame)

name_label = tk.Label(new_npc_frame, text='NPC Name:')
hp_label = tk.Label(new_npc_frame, text='NPC HP:')
ac_label = tk.Label(new_npc_frame, text='NPC AC:')
quantity_label = tk.Label(new_npc_frame, text='NPC Quantity:')
mass_update_label = tk.Label(new_npc_frame, text='Bulk Update Health Value:')

name_entry = tk.Entry(new_npc_frame, textvariable=name_var)
ac_entry = tk.Entry(new_npc_frame, textvariable=ac_var)
quantity_entry = tk.Entry(new_npc_frame, textvariable=quantity_var)
hp_entry = tk.Entry(new_npc_frame, textvariable=hp_var)
new_button = tk.Button(new_npc_frame, text='Create NPC', command=AddNewNPC)
clear_button = tk.Button(new_npc_frame, text='Clear Fields', command=ClearNewFields)
checkbox_selector = tk.Checkbutton(new_npc_frame, text='Select all checkboxes', variable=allcheck_var, 
                                   command=SelectCheckboxes)
mass_update_entry = tk.Entry(new_npc_frame, textvariable=mass_update_var)

# Define health update button
health_update_button = tk.Button(new_npc_frame, text='Update HP', command=UpdateHealth)

# Define delete all npcs
mass_delete_button = tk.Button(new_npc_frame, command=DeleteAllNPCs, text='Delete all NPCs')

# Define save and load buttons
save_button = tk.Button(new_npc_frame, text='Save NPCs to File', command=CreateSave)
load_button = tk.Button(new_npc_frame, text='Load NPCs from File', command=LoadSave)

# Define Inventory button
open_inventory_button = tk.Button(new_npc_frame, text = 'Open Inventory', command = OpenInventoryButton)

# Initialise GoldUI
goldInterface.UpdateMaster(new_npc_frame)

# Pack label frames
existing_npc_frame.pack(side='left', fill='both', expand=True)
existing_npc_frame_2.pack(side='left', fill='both', expand=True)
new_npc_frame.pack(side='left', fill='y')

# Pack new NPC widgets
name_label.grid(row=0, column=0)
hp_label.grid(row=1, column=0)
quantity_label.grid(row=2, column=0)

name_entry.grid(row=0, column=1)
hp_entry.grid(row=1, column=1)
quantity_entry.grid(row=2, column=1)

new_button.grid(row=3,column=1, pady = 5)
clear_button.grid(row = 4, column = 1)
health_update_button.grid(row = 5, column = 1, pady = 5)
checkbox_selector.grid(row = 6, column = 1)
mass_update_label.grid(row = 7, column = 0)
mass_update_entry.grid(row = 7, column = 1)
mass_delete_button.grid(row = 8, column = 1, pady = 5)
save_button.grid(row=9, column = 1)
load_button.grid(row=10, column = 1, pady = 5)
open_inventory_button.grid(row = 11, column = 1)
goldInterface.PlaceWidgets(12)
gold._NotifyCB()

# Run main loop
root.mainloop()
