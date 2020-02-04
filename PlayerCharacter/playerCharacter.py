#Author:        Dylan E. Wheeler
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



#list of core ability scores
coreAbilityScores = ["strength", "constitution", "dexterity", "intelligence", "charisma"]
minAbilityScore = 5                     #minimum score, starting score at initialization
startingAbilityPointsPerScore = 10      #player may add this many points per score to all their scores
startingAbilityPoints = startingAbilityPointsPerScore * len(coreAbilityScores)      #total of above
maxAbilityScore = 20                    #maximum ability score bonus at character creation


#list of main skills, each skill is followed by its two associated abilities
coreSkills = [["athletics", "strength", "dexterity"], 
              ["medicine", "intelligence", "dexterity"], 
              ["perception", "charisma", "intelligence"],
              ["acrobatics", "dexterity", "constitution"]]
minSkillRank = 0                #minimum additional points added to each skill besides linked abilities
startingSkillPoints = 20        #total character creation points added to skill ranks
maxSkillTotal = 100             #maximux skill score allowed (including ability bonuses)




#player character class
class playerCharacter:

    def __init__(self):
        #demographics
        self.name = "Newguy McCharacter"
        self.species = species.speciesList["human"]
        self.languages = self.species.nativeLanguages


        #abilities
        self.abilityScores = {}
        for eachScore in coreAbilityScores:         #set each score to its minumum
            self.abilityScores[eachScore] = minAbilityScore

        #skill bases (sum of two linked abilities)
        self.skillBases = {}
        for eachSkill in coreSkills:                #set each skill to the sum of its two linked abilities
            self.skillBases[eachSkill[0]] = self.abilityScores[eachSkill[1]] + self.abilityScores[eachSkill[2]]

        #skill ranks (points added to skills at character chreation and level up)
        self.skillRanks = {}
        for eachSkill in coreSkills:
            self.skillRanks[eachSkill[0]] = 0

        #skill totals (sum of skill bases and skill ranks)
        self.skills = {}
        for eachSkill in coreSkills:
            self.skills[eachSkill[0]] = self.skillBases[eachSkill[0]] + self.skillRanks[eachSkill[0]]

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
        for eachScore in coreAbilityScores:
            self.abilityScores[eachScore] += fnewAbilityScores[i]
            i += 1
        
        #update skills
        self.refreshSkillBases()
        #update hitpoints
        self.refreshHitPoints()
    #end update ability scores



    #update skill ranks
    def updateSkillRanks(self, fNewRanks):
        i = 0
        for eachSkill in coreSkills:
            self.skillRanks[eachSkill[0]] += fNewRanks[i]
            i += 1
        #update skills
        self.refreshSkills()
    #end update skill ranks

    #refresh skill bases, used if ability scores are changed
    def refreshSkillBases(self):
        for eachSkill in coreSkills:
            self.skillBases[eachSkill[0]] = self.abilityScores[eachSkill[1]] + self.abilityScores[eachSkill[2]]
        #update skill totals
        self.refreshSkills() 
    #end refresh skill bases

    #refresh skill totals, used if ability scores, skill bases, or skill ranks are changed 
    def refreshSkills(self):
        for eachSkill in coreSkills:
            self.skills[eachSkill[0]] = self.skillBases[eachSkill[0]] + self.skillRanks[eachSkill[0]]
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











#character creation screen
def characterCreation(fCharacter):
        
    print("Character Creation:")
    print()

    #remaining points to spend on abilities
    pointsLeft = startingAbilityPoints 
    #highest bonus to be added to ability scores
    maxBonus = min(maxAbilityScore - minAbilityScore, pointsLeft)
        
    abilityBonuses = {}
    for eachScore in coreAbilityScores:
        abilityBonuses[eachScore] = 0

    skillBonuses = {}
    for eachSkill in coreSkills:
        skillBonuses[eachSkill[0]] = 0

    #used when the spinbox arrows are clicked, 
    #   updates the bonuses with new value from the spinbox
    def spinboxUpdate():
        #update ability bonuses based off values in the spinboxes
        for eachScore in coreAbilityScores:
            abilityBonuses[eachScore] = int(abilityBonusSpinboxes[eachScore].get()) 

        #update skill ranks
        for eachSkill in coreSkills:
            skillBonuses[eachSkill[0]] = int(skillBonusSpinboxes[eachSkill[0]].get())

        #check how many points are left
        bonusSum = 0
        for eachScore in coreAbilityScores:
            bonusSum += abilityBonuses[eachScore]
        pointsLeft = startingAbilityPoints - bonusSum
        maxBonus = maxAbilityScore - minAbilityScore

        #don't let player spend more points than they have, resets spinbox max values
        if(pointsLeft == 0):
            for eachScore in coreAbilityScores:
                abilityBonusSpinboxes[eachScore].config(to = int(abilityBonusSpinboxes[eachScore].get()))

        #raise maximums again if player deallocates points or has points left
        else:
            for eachScore in coreAbilityScores:
                abilityBonusSpinboxes[eachScore].config(to = min(maxBonus, int(abilityBonusSpinboxes[eachScore].get()) + pointsLeft))               

        #debugging
        print(abilityBonuses, end="\t")
        print(pointsLeft, maxBonus)
    #end spinbox update


    #tkinter window for GUI character creation
    ccWindow = tkinter.Tk() #character creation window
    ccWindow.title("Character Creation")


    #give instructions for adding points to ability scores
    abilityBanner = str("Abilities:\nYou have " + str(pointsLeft) + 
                        " points to distribute amongst your ability scores.\n" + 
                        "Each score starts at " + str(minAbilityScore) + ".\n" +
                        "The maximum for each score is " + str(maxAbilityScore) + ".")
    label = tkinter.Label(text = abilityBanner).pack()
        
    #add a spinbox user uses to allocate points to each ability score
    abilityBonusSpinboxes = {}
    for eachScore in coreAbilityScores:
        label = tkinter.Label(text = eachScore.capitalize() + ":").pack() 
        abilityBonusSpinboxes[eachScore] = tkinter.Spinbox(ccWindow, from_ = 0, to = maxBonus, 
                                                           command = spinboxUpdate)
        abilityBonusSpinboxes[eachScore].pack()
    #
    label = tkinter.Label(text="").pack() #blank line


    #give instructions for adding points to skill ranks
    skillBanner = str("Skills:")
    label = tkinter.Label(text = skillBanner).pack()

    #add a spinbox user uses to allocate points to each skill rank
    skillBonusSpinboxes = {}
    for eachSkill in coreSkills:
        label = tkinter.Label(text = eachSkill[0].capitalize() + " (" +
                              eachSkill[1].capitalize() + ", " +
                              eachSkill[2].capitalize() + "):").pack()
        skillBonusSpinboxes[eachSkill[0]] = tkinter.Spinbox(ccWindow, from_ = 0, to = 100,
                                                           command = spinboxUpdate)
        skillBonusSpinboxes[eachSkill[0]].pack()
    #
    label = tkinter.Label(text="").pack() #blank line



    ccWindow.mainloop()
    #end character creation window
        
    #debugging
    print(abilityBonuses)

    #update scores
    newAbilityScores = []
    for eachScore in coreAbilityScores:
        newAbilityScores.append(abilityBonuses[eachScore])
    fCharacter.updateAbilityScores(newAbilityScores)

    newSkillRanks = []
    for eachSkill in coreSkills:
        newSkillRanks.append(skillBonuses[eachSkill[0]])
    fCharacter.updateSkillRanks(newSkillRanks)

#end character creation function
