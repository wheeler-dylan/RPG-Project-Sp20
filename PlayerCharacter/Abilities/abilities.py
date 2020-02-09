#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 09
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains the class definitions and methods for abilities 
#   abilites are used by player characters and NPCs to 
#   determine their primary capabilities.
#   Abilities also provide bonuses to skills

class ability:
    def __init__(self, fID, fName, fCategory):
        self.ID = fID
        self.name = fName
        self.category = fCategory
    #end initializer

    #print a skill to the console
    def printAbility(self):
        print("Ability:\t" + str(self.ID) + "\n" +
              "Name:\t\t" + str(self.name) + "\n" +
              "Type:\t\t" + str(self.category) + "\n")
    #end print skill

#end skill definition


#load skills from game configuration file
coreAbilities = {}
abilityConfig = open("./PlayerCharacter/Abilities/abilities.gameconfig")
for eachLine in abilityConfig:
    abilityData = str(eachLine.replace("\n", "")).split(", ")
    thisAbility = ability(abilityData[0], abilityData[1], abilityData[2])
    coreAbilities[thisAbility.ID] = thisAbility
#end load


