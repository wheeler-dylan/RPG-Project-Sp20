#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 09
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains the class definitions and methods for skills 
#   skills are used by player characters and NPCs to 
#   determine the success of tasks performed in the game

import sys
sys.path.append('./PlayerCharacter/Abilities')
import abilities

class skill:
    def __init__(self, fID, fName, fMainAbility, fSecondaryAbility, fCategory):
        self.ID = fID
        self.name = fName
        self.mainAbility = fMainAbility
        self.secondaryAbility = fSecondaryAbility
        self.category = fCategory
    #end initializer

    #print a skill to the console
    def printSkill(self):
        print("Skill:\t\t" + str(self.ID) + "\n" +
              "Name:\t\t" + str(self.name) + "\n" +
              "Main Abil:\t" + str(self.mainAbility.name) + "\n" +
              "Sec Abil:\t" + str(self.secondaryAbility.name) + "\n" +
              "Type:\t\t" + str(self.category) + "\n")
    #end print skill

#end skill definition


#load skills from game configuration file
coreSkills = {}
skillsConfig = open("./PlayerCharacter/Skills/skills.gameconfig")
for eachLine in skillsConfig:
    skillData = str(eachLine.replace("\n", "")).split(", ")
    thisSkill = skill(skillData[0], 
                      skillData[1], 
                      abilities.coreAbilities[skillData[2]], 
                      abilities.coreAbilities[skillData[3]], 
                      skillData[4])
    coreSkills[thisSkill.ID] = thisSkill
#end load


