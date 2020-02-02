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
        open(fFile)
        #TODO
    #end load item from file

    #generate an item with only a name and description
    def quickBuild(self):
        self.name = input("Enter item name:")
        self.description = input("Describe the item:") 
    #end quick build

