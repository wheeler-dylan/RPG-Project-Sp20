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
sys.path.append('./PlayerCharacter/Skills')
import skills
sys.path.append('./PlayerCharacter/Abilities')
import abilities


#list of core ability scores
#abilities.coreAbilities.values() = ["strength", "constitution", "dexterity", "intelligence", "charisma"]






import characterCreation


#player character class
class playerCharacter:

    def __init__(self):
        #demographics
        self.name = "Newguy McCharacter"
        self.species = species.speciesList["human"]
        self.languages = self.species.nativeLanguages


        #abilities
        self.abilityScores = {}
        for eachAbility in abilities.coreAbilities.values():         #set each score to its minumum
            self.abilityScores[eachAbility.ID] = characterCreation.minAbilityScore

        #skill bases (sum of two linked abilities)
        self.skillBases = {}
        for eachSkill in skills.coreSkills.values():                #set each skill to the sum of its two linked abilities
            self.skillBases[eachSkill.ID] = (self.abilityScores[eachSkill.mainAbility.ID] + 
                                             self.abilityScores[eachSkill.secondaryAbility.ID])

        #skill ranks (points added to skills at character chreation and level up)
        self.skillRanks = {}
        for eachSkill in skills.coreSkills.values():
            self.skillRanks[eachSkill.ID] = 0

        #skill totals (sum of skill bases and skill ranks)
        self.skills = {}
        for eachSkill in skills.coreSkills.values():
            self.skills[eachSkill.ID] = self.skillBases[eachSkill.ID] + self.skillRanks[eachSkill.ID]

        #combat stats
        self.hitPointTotal = (self.abilityScores["strength"] + self. abilityScores["constitution"]) * 2
        self.hitPoints = {}
        for eachHitbox in self.species.hitboxes:
            self.hitPoints[eachHitbox] = int(self.hitPointTotal * (self.species.hitboxes[eachHitbox]/100))
        speed = 1

        #inventory
        self.inventory = []

    #end initializer



    #update ability scores
    def updateAbilityScores(self, fnewAbilityScores):
        i = 0
        for eachAbility in abilities.coreAbilities.values():
            self.abilityScores[eachAbility.ID] += fnewAbilityScores[i]
            i += 1
        
        #update skills
        self.refreshSkillBases()
        #update hitpoints
        self.refreshHitPoints()
    #end update ability scores



    #update skill ranks
    def updateSkillRanks(self, fNewRanks):
        i = 0
        for eachSkill in skills.coreSkills.values():
            self.skillRanks[eachSkill.ID] += fNewRanks[i]
            i += 1
        #update skills
        self.refreshSkills()
    #end update skill ranks

    #refresh skill bases, used if ability scores are changed
    def refreshSkillBases(self):
        for eachSkill in skills.coreSkills.values():
            self.skillBases[eachSkill.ID] = (self.abilityScores[eachSkill.mainAbility.ID] + 
                                             self.abilityScores[eachSkill.secondaryAbility.ID])
        #update skill totals
        self.refreshSkills() 
    #end refresh skill bases

    #refresh skill totals, used if ability scores, skill bases, or skill ranks are changed 
    def refreshSkills(self):
        for eachSkill in skills.coreSkills.values():
            self.skills[eachSkill.ID] = self.skillBases[eachSkill.ID] + self.skillRanks[eachSkill.ID]
    #end skill refresh



    #refresh hitpoints, used if ability scores change
    def refreshHitPoints(self):
        self.hitPointTotal = (self.abilityScores["strength"] + self. abilityScores["constitution"])
        for eachHitbox in self.species.hitboxes:
            self.hitPoints[eachHitbox] = int(self.hitPointTotal * (self.species.hitboxes[eachHitbox]/100))
    #end refresh hitpoints



    #add item to inventory
    def collectItem(self, fItem):
        self.inventory.append(fItem)
    #end add item to inventory

#end player character class
