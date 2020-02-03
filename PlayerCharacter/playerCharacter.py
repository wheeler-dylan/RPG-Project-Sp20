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


#establish starting score for each new player characters ability scores
#   indicates minimum value of an ability score at start
minAbilityScore = 10

#establish number of character creations points allocated when
#   creating a new character, these points will be divided amongst the 
#   character ability scores
startingAbilityPoints = 120

#establish maximum ability score allowed
maxAbilityScore = 100

#list of core ability scores
coreAbilityScores = ["strength", "consitution", "dexterity", "intelligence", "charisma"]

#list of main skills
#TODO


#player character class
class playerCharacter:
    #global minAbilityScore
    #global coreAbilityScores
    
    def __init__(self):
        #demographics
        self.name = "Newguy McCharacter"
        self.species = "Human"

        #abilities
        self.abilityScores = {}
        for eachScore in coreAbilityScores:
            self.abilityScores[eachScore] = minAbilityScore 

        #inventory
        self.inventory = []
    #end initializer

    #update ability scores
    def updateAbilityScores(self, fNewScores):
        i = 0
        for eachScore in coreAbilityScores:
            self.abilityScores[eachScore] += fNewScores[i]
            i += 1
    #end update ability scores

    #add item to inventory
    def collectItem(self, fItem):
        self.inventory.append(fItem)
    #end add item to inventory

    #character creation screen
    def characterCreation(self):
        
        print("Character Creation:")
        print()

        #remaining points to spend on abilities
        pointsLeft = startingAbilityPoints 
        #highest bonus to be added to ability scores
        maxBonus = min(maxAbilityScore - minAbilityScore, pointsLeft)
        
        abilityBonuses = {}
        for eachScore in coreAbilityScores:
            abilityBonuses[eachScore] = 0

        #used when the spinbox arrows are clicked, 
        #   updates the bonuses with new value from the spinbox
        def updateBonusesFromSpinbox():
            global startingAbilityPoints, maxAbilityScore, minAbilityScore, pointsLeft, maxBonus

            #update bonuses based off values in the spinboxes
            for eachScore in coreAbilityScores:
                abilityBonuses[eachScore] = int(abilityBonusSpinboxes[eachScore].get()) 

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


        #tkinter window for GUI character creation
        ccWindow = tkinter.Tk() #character creation window
        ccWindow.title("Character Creation")

        instructionsText = str("You have " + str(pointsLeft) + 
                " points to distribute amongst your ability scores.\n" + 
                "Each score starts at " + str(minAbilityScore) + ".\n" +
                "The maximum for each score is " + str(maxAbilityScore) + ".")

        label_instructions = tkinter.Label(text = instructionsText).pack()
        

        #the following section use spinboxes to update the bonuses the player 
        #   would like to add to each ability
        abilityBonusSpinboxes = {}
        for eachScore in coreAbilityScores:
            label = tkinter.Label(text = eachScore.capitalize() + ":").pack() 
            abilityBonusSpinboxes[eachScore] = tkinter.Spinbox(ccWindow, from_ = 0, to = maxBonus, command = updateBonusesFromSpinbox)
            abilityBonusSpinboxes[eachScore].pack()

        ccWindow.mainloop()
        #end character creation window
        
        #debugging
        print(abilityBonuses)

        #update scores
        newScores = []
        for eachScore in coreAbilityScores:
            newScores.append(abilityBonuses[eachScore])
        self.updateAbilityScores(newScores)

    #end character creation function

#end player character class
