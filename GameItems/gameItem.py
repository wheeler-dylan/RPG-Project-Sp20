#Author:        Dylan E. Wheeler
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

#item class 
class gameItem():
    def __init__(self):
        self.name = "item"
        self.description = "description"
        self.actions = []
        self.subitems = []
    #end initializer


    #print item to console for debugging
    def printItem(self):
        #print("\n-------------------------\n" +
        print("Game Item:\n" +
              "Name:\t" + str(self.name) + "\n" +
              "\nDescription:\n" +
              str(self.description) + "\n" +
              "\nAvailable Actions:")
        if (len(self.actions) == 0):
            print("None")
        else:
            for eachAction in self.actions:
                print(eachAction.__name__)
        print("\nsubitems:")
        if (len(self.subitems) == 0):
            print("None")
        else:
            for eachItem in self.subitems:
                print(str(eachItem.name))
        #print("\n-------------------------\n")


    #open an item stored in host device
    def loadItemFromFile(self, fFile):
        for eachLine in fFile:

            if "name: " in eachLine:
                thisLine = str(eachLine.replace("name: ", "").replace("\n", ""))
                self.name = thisLine

            if "description: " in eachLine:
                thisLine = str(eachLine.replace("description: ", "").replace("\n", ""))
                self.description = thisLine

            if "actions: " in eachLine:
                thisLine = str(eachLine.replace("actions: ", "").replace("\n", ""))
                theseActions = thisLine.split(", ")

                for eachAction in theseActions:
                    if eachAction in gameItemActionDictionary.validActions:
                        self.actions.append(gameItemActionDictionary.validActions[eachAction]) 

            if "subitems: " in eachLine: 
                thisLine = str(eachLine.replace("subitems: ", "").replace("\n", "").replace(" ", ""))
                theseItems = thisLine.split(", ")

                for eachItem in theseItems:
                    if (len(eachItem) > 0):
                        thisItem = gameItem()
                        thisItemFile = open("./GameItems/" + str(eachItem) + ".gmitm")
                        if (thisItemFile):
                            thisItem.loadItemFromFile(thisItemFile)
                            self.subitems.append(thisItem) 

    #end load item from file


    #save item to a file on host device
    def saveItemToFile(self):
        fileName = "./GameItems/" + str(self.name).lower().replace(" ", "") + ".gmitm"
        print(fileName)
        file = open(fileName, "w+")
        file.write("name: " + str(self.name) + "\n")
        file.write("description: " + str(self.description) + "\n")
        file.write("actions: ")
        for eachAction in self.actions:
            file.write(eachAction.__name__)
            file.write(", ")
        file.write("\n")
        file.write("subitems: ")
    #end save item


    #generate an item with only a name and description
    def quickBuild(self):
        self.name = input("Enter item name:")
        self.description = input("Describe the item:") 
    #end quick build


#end game item class


#function to get a list of items from all saved items
from glob import glob
def loadItemsList():
    itemsList = []
    
    for eachFile in glob("./GameItems/*.gmitm"): #search game items directory for all gmitm files
        thisItem = gameItem()
        thisItem.loadItemFromFile(open(eachFile))
        itemsList.append(thisItem)
    #

    return itemsList
#end load item list




##### Game Item Creation Window (GUI) #####
def gameItemCreation(fGameItem):

    #variables to store updated item information
    newName = ""
    newDescription = ""

    gameItemCreationWindow = tkinter.Tk()
    gameItemCreationWindow.title("Game Item Creation")
    gameItemCreationWindow.geometry('500x250')

    #enter name
    label = tkinter.Label(text = "Name:").pack()
    nameInput = tkinter.Entry()
    nameInput.pack()

    #enter description
    label = tkinter.Label(text = "Decription:").pack()
    descriptionInput = tkinter.Entry()
    descriptionInput.pack()

    #select item actions
    label = tkinter.Label(text = "Actions:").pack()

    #load selectable actions into list
    actionList = []
    actionCheckboxes = {}
    for eachAction in gameItemActionDictionary.validActions:
        actionCheckboxes[eachAction] = ttk.Checkbutton(text = str(eachAction))
        actionCheckboxes[eachAction].state(['!alternate'])
        actionCheckboxes[eachAction].pack()

    #select subitems
    label = tkinter.Label(text = "Subitems:").pack()

    #load selectable subitems into list
    subitemList = []
    subitemCheckboxes = {}
    allItems = loadItemsList()
    for eachItem in allItems:
        subitemCheckboxes[eachItem.name] = ttk.Checkbutton(
            text = str(eachItem.name))
        subitemCheckboxes[eachItem.name].state(['!alternate'])
        subitemCheckboxes[eachItem.name].pack()

    #when window is closed
    def windowExit():
        #save inputs
        fGameItem.name = nameInput.get()
        fGameItem.description = descriptionInput.get()
        
        #save actions
        for eachAction in gameItemActionDictionary.validActions:
            if (actionCheckboxes[eachAction].instate(['selected'])):
                fGameItem.actions.append(
                    gameItemActionDictionary.validActions[eachAction])

        #save subitems
        for eachItem in allItems:
            if (subitemCheckboxes[eachItem.name].instate(['selected'])):
                fGameItem.subitems.append(eachItem)
        
        #close window
        gameItemCreationWindow.destroy()
    #called on close
    gameItemCreationWindow.protocol("WM_DELETE_WINDOW", windowExit) 
    

    #execute window
    gameItemCreationWindow.mainloop()

#end game item creation GUI