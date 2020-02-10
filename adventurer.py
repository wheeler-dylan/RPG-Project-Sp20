#Author:        John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:  2020 02 10
#Course:        CSC424 - Software Engineering II
#Prof:      Dr. A. Louise Perkins
#
#Rudamentary player object file for network testing purposes 

# for creating a unique ID for each object
#
import uuid

# Basic player class
#
class Adventurer():
    def __init__(self, name, fate, hitpoints, onTheMind):
        self.ObjectID = uuid.uuid1()
        self.name = name
        self.fate = fate
        self.hitpoints = hitpoints
        self.onTheMind = onTheMind
        
    def getObjectID(self):
        return self.ObjectID
    
    # Function for setting what will be spoken next
    #
    def think(self):
        self.onTheMind = input("Enter what you wish to say.")
    
    # Function for the player to speak what is queued on their mind
    #
    def speak(self):
        print(self.onTheMind)
    
    # Basic player introduction to be spoken
    #
    def introduce(self):
        print("Hello, I am " + self.name + ", and I am a " + self.fate + ".")