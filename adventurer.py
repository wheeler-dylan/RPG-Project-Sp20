#Author:        John P Armentor
#Date:          2019 01 30
#Course:        CSC242 - Software Engineering II
#Prof:         Dr. A. Louise Perkins

#Rudamentary player object file for network testing purposes 

# Basic player class
#
class Adventurer():
    def __init__(self, name, fate, hitpoints, onTheMind):
        self.name = name
        self.fate = fate
        self.hitpoints = hitpoints
        self.onTheMind = onTheMind
    
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