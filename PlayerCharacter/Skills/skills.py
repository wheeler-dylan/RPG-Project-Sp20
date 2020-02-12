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
    def __init__(self, f_id, f_name, f_main_ability, f_secondary_ability, f_category):
        self.id = f_id
        self.name = f_name
        self.main_ability = f_main_ability
        self.secondary_ability = f_secondary_ability
        self.category = f_category
    #end initializer

    #print a skill to the console
    def print_skill(self):
        print("Skill:\t\t" + str(self.id) + "\n" +
              "Name:\t\t" + str(self.name) + "\n" +
              "Main Abil:\t" + str(self.main_ability.name) + "\n" +
              "Sec Abil:\t" + str(self.secondary_ability.name) + "\n" +
              "Type:\t\t" + str(self.category) + "\n")
    #end print skill

#end skill definition


#load skills from game configuration file
core_skills = {}
skills_config = open("./PlayerCharacter/Skills/skills.gameconfig")
for each_line in skills_config:
    skill_data = str(each_line.replace("\n", "")).split(", ")
    this_skill = skill(skill_data[0], 
                      skill_data[1], 
                      abilities.core_abilities[skill_data[2]], 
                      abilities.core_abilities[skill_data[3]], 
                      skill_data[4])
    core_skills[this_skill.id] = this_skill
#end load


