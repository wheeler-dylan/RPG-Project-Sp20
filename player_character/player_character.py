#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 01 30
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class and methods for initializing a 
#   player character game object.
#   
#   A player character (PC) is an entity controled by the remote users,
#       as opposed to the host user, that acts as the main protagonist of the game.
#   
#   A PC has several main statistics (Abilities) that it uses to 
#       affect its interactions with the game environement. 
#       These abilities indicate the character's prowess in feats
#       such as strength, agility, and the like.
#
#   A PC will also have an inventory of items it collects during the game.
#
#   Future implementation of this class will define methods to
#       engage in activities such as combat.

import tkinter
import species 
import sys
sys.path.append('./player_character/abilities')
import abilities
sys.path.append('./player_character/skills')
import skills
import uuid


#list of core ability scores
#abilities.coreAbilities.values() = ["strength", "constitution", "dexterity", "intelligence", "charisma"]






import character_creation


#player character class
class PlayerCharacter:

    def __init__(self):
        #demographics
        self.object_id = uuid.uuid1()
        self.name = "Newguy McCharacter"
        self.species = species.species_list["human"]
        self.languages = self.species.native_languages


        #abilities
        self.ability_scores = {}
        for each_ability in abilities.core_abilities.values():         #set each score to its minumum
            self.ability_scores[each_ability.id] = character_creation.min_ability_score

        #skill bases (sum of two linked abilities)
        self.skill_bases = {}
        for each_skill in skills.core_skills.values():                #set each skill to the sum of its two linked abilities
            self.skill_bases[each_skill.id] = (self.ability_scores[each_skill.main_ability.id] + 
                                             self.ability_scores[each_skill.secondary_ability.id])

        #skill ranks (points added to skills at character chreation and level up)
        self.skill_ranks = {}
        for each_skill in skills.core_skills.values():
            self.skill_ranks[each_skill.id] = 0

        #skill totals (sum of skill bases and skill ranks)
        self.skills = {}
        for each_skill in skills.core_skills.values():
            self.skills[each_skill.id] = self.skill_bases[each_skill.id] + self.skill_ranks[each_skill.id]

        #combat stats
        self.hit_point_total = (self.ability_scores["strength"] + self. ability_scores["constitution"]) * 2
        self.hit_points = {}
        for each_hitbox in self.species.hitboxes:
            self.hit_points[each_hitbox] = int(self.hit_point_total * (self.species.hitboxes[each_hitbox]/100))
        self.speed = self.ability_scores["constitution"] * 2

        #inventory
        self.inventory = []

    #end initializer



    #update ability scores
    def update_ability_scores(self, fnew_ability_scores):
        i = 0
        for each_ability in abilities.core_abilities.values():
            self.ability_scores[each_ability.id] += fnew_ability_scores[i]
            i += 1
        
        #update skills
        self.refresh_skill_bases()
        #update hitpoints
        self.refresh_hit_points()
    #end update ability scores



    #update skill ranks
    def update_skill_ranks(self, f_new_ranks):
        i = 0
        for each_skill in skills.core_skills.values():
            self.skill_ranks[each_skill.id] += f_new_ranks[i]
            i += 1
        #update skills
        self.refresh_skills()
    #end update skill ranks

    #refresh skill bases, used if ability scores are changed
    def refresh_skill_bases(self):
        for each_skill in skills.core_skills.values():
            self.skill_bases[each_skill.id] = (self.ability_scores[each_skill.main_ability.id] + 
                                             self.ability_scores[each_skill.secondary_ability.id])
        #update skill totals
        self.refresh_skills() 
    #end refresh skill bases

    #refresh skill totals, used if ability scores, skill bases, or skill ranks are changed 
    def refresh_skills(self):
        for each_skill in skills.core_skills.values():
            self.skills[each_skill.id] = self.skill_bases[each_skill.id] + self.skill_ranks[each_skill.id]
    #end skill refresh



    #refresh hitpoints, used if ability scores change
    def refresh_hit_points(self):
        self.hit_point_total = (self.ability_scores["strength"] + self. ability_scores["constitution"])
        for each_hitbox in self.species.hitboxes:
            self.hit_points[each_hitbox] = int(self.hit_point_total * (self.species.hitboxes[each_hitbox]/100))
    #end refresh hitpoints



    #add item to inventory
    def collect_item(self, f_item):
        self.inventory.append(f_item)
    #end add item to inventory

#end player character class
