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


#player character class
class playerCharacter:
    def __init__(self):
        #demographics
        self.name = "Newguy McCharacter"

        #abilities
        global minAbilityScore
        self.strengthScore = minAbilityScore
        self.constitutionScore = minAbilityScore
        self.dexterityScore = minAbilityScore
        self.intelligenceScore = minAbilityScore
        
        #inventory
        self.inventory = []
    
    #end initializer

    #update ability scores
    def updateAbilities(self, fStr, fCon, fDex, fInt):
        self.strengthScore += fStr
        self.constitutionScore += fCon
        self.dexterityScore += fDex
        self.intelligenceScore += fInt
    #end update ability scores

    #add item to inventory
    def collectItem(self, fItem):
        self.inventory.append(fItem)
    #end add item to inventory

    #character creation screen
    def characterCreation(self):
        global startingAbilityPoints
        global maxAbilityScore
        global minAbilityScore
        
        print("Character Creation:")
        print()

        #remaining points to spend on abilities
        pointsLeft = startingAbilityPoints 
        #highest bonus to be added to ability scores
        maxBonus = min(maxAbilityScore - minAbilityScore, pointsLeft)
        

        #used when the spinbox arrows are clicked, 
        #   updates the bonuses with new value from the spinbox
        def updateBonusesFromSpinbox():
            global strengthBonus, constitutionBonus, dexterityBonus, intelligenceBonus
            global maxBonus, startingAbilityPoints, maxAbilityScore, minAbilityScore, pointsLeft
            strengthBonus = int(spinbox_strengthBonus.get())
            constitutionBonus = int(spinbox_constitutionBonus.get())
            dexterityBonus = int(spinbox_dexterityBonus.get())
            intelligenceBonus = int(spinbox_intelligenceBonus.get())
            pointsLeft = startingAbilityPoints - (strengthBonus + constitutionBonus + dexterityBonus + intelligenceBonus)
            maxBonus = min(maxAbilityScore - minAbilityScore, pointsLeft)
            if(pointsLeft == 0):
                spinbox_strengthBonus.config(to = int(spinbox_strengthBonus.get()))
                spinbox_constitutionBonus.config(to = int(spinbox_constitutionBonus.get()))
                spinbox_dexterityBonus.config(to = int(spinbox_dexterityBonus.get()))
                spinbox_intelligenceBonus.config(to = int(spinbox_intelligenceBonus.get()))
            else:
                spinbox_strengthBonus.config(to = max(maxBonus, int(spinbox_strengthBonus.get()) + pointsLeft))
                spinbox_constitutionBonus.config(to = max(maxBonus, int(spinbox_constitutionBonus.get()) + pointsLeft))
                spinbox_dexterityBonus.config(to = max(maxBonus, int(spinbox_dexterityBonus.get()) + pointsLeft))
                spinbox_intelligenceBonus.config(to = max(maxBonus, int(spinbox_intelligenceBonus.get()) + pointsLeft))

            print(strengthBonus, constitutionBonus, dexterityBonus, intelligenceBonus, pointsLeft, maxBonus)


        #tkinter window for GUI character creation
        ccWindow = tkinter.Tk() #character creation window
        ccWindow.title("Character Creation")

        instructionsText = str("You have " + str(pointsLeft) + 
                " points to distribute amongst your ability scores.\n" + 
                "Each score starts at " + str(minAbilityScore) + ".\n" +
                "The maximum for each score is " + str(maxAbilityScore) + ".")

        label_instructions = tkinter.Label(text = instructionsText).pack()
        

        #the following section use spinboxes to update the bonuses the player 
        #   would like to grant to each ability

        #strength            
        spinbox_strengthBonus = tkinter.Spinbox(ccWindow, from_ = 0, to = maxBonus, command = updateBonusesFromSpinbox)
        spinbox_strengthBonus.pack() 
        
        #constitution
        spinbox_constitutionBonus = tkinter.Spinbox(ccWindow, from_ = 0, to = maxBonus, command = updateBonusesFromSpinbox)
        spinbox_constitutionBonus.pack() 
        
        #dexterity
        spinbox_dexterityBonus = tkinter.Spinbox(ccWindow, from_ = 0, to = maxBonus, command = updateBonusesFromSpinbox)
        spinbox_dexterityBonus.pack() 
        
        #intelligence
        spinbox_intelligenceBonus = tkinter.Spinbox(ccWindow, from_ = 0, to = maxBonus, command = updateBonusesFromSpinbox)
        spinbox_intelligenceBonus.pack() 

        ccWindow.mainloop()
        #end character creation window


        #TODO: input validation to ensure points are not greater than maximum

        print(strengthBonus, constitutionBonus, dexterityBonus, intelligenceBonus, pointsLeft, maxBonus)

        #update scores
        self.updateAbilities(strengthBonus, constitutionBonus, dexterityBonus, intelligenceBonus)

    #end character creation function

#end player character class
