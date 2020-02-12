#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 01 30
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class and methods for initializing a 
#   game item object. Game items represent items a player 
#   character can collect throughout the game, such as weapons
#   and armor.
#
#   Game items will be able to be created by a game master (GM), and
#       stored on the GM host device, and stored devices will be loaded 
#       at runtime. (Future implementation should only load items as they 
#       are needed in order to save RAM space.)

import tkinter 
from tkinter import ttk

import gameItemActionDictionary

import uuid

#item class 
class gameItem():
    def __init__(self):
        self.object_id = uuid.uuid1()
        self.name = "item"
        self.description = "description"
        self.actions = []
        self.sub_items = []
    #end initializer


    #print item to console for debugging
    def print_item(self):
        #print("\n-------------------------\n" +
        print("Game Item:\n" +
              "Name:\t" + str(self.name) + "\n" +
              "\nDescription:\n" +
              str(self.description) + "\n" +
              "\nAvailable Actions:")
        if (len(self.actions) == 0):
            print("None")
        else:
            for each_action in self.actions:
                print(each_action.__name__)
        print("\nsubitems:")
        if (len(self.sub_items) == 0):
            print("None")
        else:
            for each_item in self.sub_items:
                print(str(each_tem.name))
        #print("\n-------------------------\n")


    #open an item stored in host device
    def load_item_from_file(self, f_file):
        for each_line in f_file:

            if "name: " in each_line:
                this_line = str(each_line.replace("name: ", "").replace("\n", ""))
                self.name = this_line

            if "description: " in each_line:
                this_line = str(each_line.replace("description: ", "").replace("\n", ""))
                self.description = this_line

            if "actions: " in each_line:
                this_line = str(each_line.replace("actions: ", "").replace("\n", ""))
                these_actions = this_line.split(", ")

                for each_action in these_actions:
                    if each_action in game_item_action_dictionary.valid_actions:
                        self.actions.append(game_item_action_dictionary.valid_actions[each_action]) 

            if "subitems: " in each_line: 
                this_line = str(each_line.replace("subitems: ", "").replace("\n", "").replace(" ", ""))
                these_items = this_line.split(", ")

                for each_item in these_items:
                    if (len(each_item) > 0):
                        this_item = game_item()
                        this_item_file = open("./GameItems/" + str(each_item) + ".gmitm")
                        if (this_item_file):
                            this_item.load_item_from_file(this_item_file)
                            self.sub_items.append(this_item) 

    #end load item from file


    #save item to a file on host device
    def save_item_to_file(self):
        file_name = "./GameItems/" + str(self.name).lower().replace(" ", "") + ".gmitm"
        print(file_name)
        file = open(file_name, "w+")
        file.write("name: " + str(self.name) + "\n")
        file.write("description: " + str(self.description) + "\n")
        file.write("actions: ")
        for each_action in self.actions:
            file.write(each_action.__name__)
            file.write(", ")
        file.write("\n")
        file.write("subitems: ")
    #end save item


    #generate an item with only a name and description
    def quick_build(self):
        self.name = input("Enter item name:")
        self.description = input("Describe the item:") 
    #end quick build


#end game item class


#function to get a list of items from all saved items
from glob import glob
def load_items_list():
    items_list = []
    
    for each_file in glob("./GameItems/*.gmitm"): #search game items directory for all gmitm files
        this_item = game_item()
        this_item.load_item_from_file(open(each_file))
        items_list.append(this_item)
    #

    return items_list
#end load item list




##### Game Item Creation Window (GUI) #####
def game_item_creation(f_game_item):

    #variables to store updated item information
    new_name = ""
    new_description = ""

    game_item_creation_window = tkinter.Tk()
    game_item_creation_window.title("Game Item Creation")
    game_item_creation_window.geometry('500x250')

    #enter name
    label = tkinter.Label(text = "Name:").pack()
    name_input = tkinter.Entry()
    name_input.pack()

    #enter description
    label = tkinter.Label(text = "Decription:").pack()
    description_input = tkinter.Entry()
    description_input.pack()

    #select item actions
    label = tkinter.Label(text = "Actions:").pack()

    #load selectable actions into list
    action_list = []
    action_checkboxes = {}
    for each_action in game_item_action_dictionary.valid_actions:
        action_checkboxes[each_action] = ttk.Checkbutton(text = str(each_action))
        action_checkboxes[each_action].state(['!alternate'])
        action_checkboxes[each_action].pack()

    #select subitems
    label = tkinter.Label(text = "Subitems:").pack()

    #load selectable subitems into list
    subitem_list = []
    subitem_checkboxes = {}
    all_items = load_items_list()
    for each_item in all_items:
        subitem_checkboxes[each_item.name] = ttk.Checkbutton(
            text = str(each_item.name))
        subitem_checkboxes[each_item.name].state(['!alternate'])
        subitem_checkboxes[each_item.name].pack()

    #when window is closed
    def window_exit():
        #save inputs
        f_game_item.name = name_input.get()
        f_game_item.description = description_input.get()
        
        #save actions
        for each_action in game_item_action_dictionary.valid_actions:
            if (action_checkboxes[each_action].instate(['selected'])):
                f_game_item.actions.append(
                    game_item_action_dictionary.valid_actions[each_action])

        #save subitems
        for each_item in all_items:
            if (subitem_checkboxes[each_item.name].instate(['selected'])):
                f_game_item.subitems.append(each_item)
        
        #close window
        game_item_creation_window.destroy()
    #called on close
    game_item_creation_window.protocol("WM_DELETE_WINDOW", window_exit) 
    

    #execute window
    game_item_creation_window.mainloop()

#end game item creation GUI