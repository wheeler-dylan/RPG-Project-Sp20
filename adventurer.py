#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:  2020 02 10
#Course:    CSC424 - Software Engineering II
#Prof:      Dr. A. Louise Perkins
#
#Rudamentary player object file for network testing purposes 

# for creating a unique ID for each object
#
import uuid

# Basic player class
#
class Adventurer():
    def __init__(self, name, fate, hitpoints, on_the_mind):
        self.object_id = uuid.uuid1()
        self.name = name
        self.fate = fate
        self.hitpoints = hitpoints
        self.on_the_mind = on_the_mind
    
    def get_object_id(self):
        return self.object_id
    
    # Function for setting what will be spoken next
    #
    def think(self):
        self.on_the_mind = input("Enter what you wish to say.")
    
    # Function for the player to speak what is queued on their mind
    #
    def speak(self):
        print(self.on_the_mind)
    
    # Basic player introduction to be spoken
    #
    def introduce(self):
        print("Hello, I am " + self.name + ", and I am a " + self.fate + ".")