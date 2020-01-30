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

        #remaining points to spend on abilities
        pointsLeft = startingAbilityPoints 
        
        print("Character Creation:")
        print("You have " + str(startingAbilityPoints) + " points to distribute " +
              "amongst your ability scores.\n" + 
              "Each score starts at " + str(minAbilityScore) + ".\n" +
              "The maximum for each score is " + str(maxAbilityScore) + ".")

        #TODO: future implementation goes here: develop tkinter window for GUI character creation

        #TEMP: enter point distributions in console
        #Strength
        print("Enter Strength score (points remaining: " + str(pointsLeft) + ")")
        inputStr = int(input())
        pointsLeft -= inputStr
        
        #Constitution
        print("Enter Constitution score (points remaining: " + str(pointsLeft) + ")")
        inputCon = int(input())
        pointsLeft -= inputCon
        
        #Dexterity
        print("Enter Dexterity score (points remaining: " + str(pointsLeft) + ")")
        inputDex = int(input())
        pointsLeft -= inputDex
        
        #Intelligence
        print("Enter Intelligence score (points remaining: " + str(pointsLeft) + ")")
        inputInt = int(input())
        pointsLeft -= inputInt

        #TODO: input validation to ensure points are not greater than maximum

        #update scores
        self.updateAbilities(inputStr, inputCon, inputDex, inputInt)




#end player character class