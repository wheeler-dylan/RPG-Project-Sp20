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

import gameItemActionDictionary

#item class 
class gameItem():
    def __init__(self):
        self.name = "item"
        self.description = "description"
        self.actions = []
        self.subItems = []
    #end initializer

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
                #print(theseActions) #debugging
                for eachAction in theseActions:
                    #print("for each action in these actions") #debugging
                    if eachAction in gameItemActionDictionary.validActions:
                        #print("action found!") #debugging
                        self.actions.append(gameItemActionDictionary.validActions[eachAction]) 
            #TODO: add subitems
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

    #generate an item with only a name and description
    def quickBuild(self):
        self.name = input("Enter item name:")
        self.description = input("Describe the item:") 
    #end quick build

#end game item class


