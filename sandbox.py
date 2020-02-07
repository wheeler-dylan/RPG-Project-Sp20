############################
# sandbox file for testing #
############################

import sys
sys.path.append('./PlayerCharacter')
import playerCharacter
import characterCreation 
sys.path.append('./GameItems')
import gameItem
import gameItemActionDictionary


print("-------------------------Running sandbox.py-------------------------\n\n")

command = ""
player1 = playerCharacter.playerCharacter()

instructions = ("\n\nsandbox commands:\n" +
                "exit:\tclose the program\n" +
                "help:\tprint list of commands\n" +
                "\n----- Player Character Commands -----\n" +
                "build:\tcreate a new character with gui\n" +
                #"quick:\tinstantly create a basic character\n" +
                "abils:\toutput the character's abilities\n" +
                "skills:\toutput the character's skills\n" +
                #"sheet:\toutput all the character's stats\n\n\n" +
                "\n----- Game Item Commands -----\n" +
                "look:\tview a list of all items in the game items folder\n" +
                "find:\tload an example item (iron sword)" +
                "\n")
print(instructions)

while(command != "exit"):
    command = input()

    #input command switch
    if (command == "help"):         #output valid commands for sandbox
        print("-------------------------\n")
        print(instructions)
        print("\n-------------------------\n")

    if (command == "build"):        #tests Character Creation GUI
        characterCreation.characterCreation(player1)

    elif (command == "abils"):      #ensures ability scores have been updated
        print("-------------------------\n")
        for eachScore in playerCharacter.coreAbilityScores:
            print(str(eachScore)+":\t"+str(player1.abilityScores[eachScore]))
        print("\n-------------------------\n")
        

    elif (command == "skills"):     #ensures skills have been updated
        print("-------------------------\n")
        for eachSkill in playerCharacter.coreSkills:
            print(str(eachSkill[0])+"\t"+str(player1.skills[eachSkill[0]]))
        print("\n-------------------------\n")

    elif (command == "look"):       #tests function to get a list of game items from folder
        print("-------------------------\n")
        itemList = gameItem.loadItemsList()
        for eachItem in itemList:
            print(eachItem.name)
        print("\n-------------------------\n")

    elif (command == "find"):       #tests game item load and print
        print("-------------------------\n")
        ironSword = gameItem.gameItem()
        ironSword.loadItemFromFile(open("./GameItems/ironsword.gmitm"))
        ironSword.printItem()
        print("\n-------------------------\n")

    #end command switch
        























"""
#create new PC
Etrius = playerCharacter.playerCharacter()
#playerCharacter.characterCreation(Etrius)

#display ability score dictionary and skills dictionary
print(Etrius.abilityScores)
print(Etrius.skills)

#Etrius.updateAbilityScores([50,3,5,7,11])
#print(Etrius.abilityScores)
#print(Etrius.skills)
#Etrius.updateSkillRanks([33,44,55])

Etrius.abilityScores["strength"] = 15
Etrius.abilityScores["constitution"] = 15

Etrius.updateAbilityScores([0,0,0,0,0])

print(Etrius.abilityScores)
print(Etrius.skills)

print(Etrius.hitPoints)
"""

"""
#update scores
print("Updating scores (add 5 to each)")
newScores = []
for score in playerCharacter.coreAbilityScores:
    newScores.append(5)
Etrius.updateAbilityScores(newScores)

print(Etrius.abilityScores)
"""

"""
#display scores
print("Strength: " + str(Etrius.strengthScore))
print("Constitution: " + str(Etrius.constitutionScore))
print("Dexterity: " + str(Etrius.dexterityScore))
print("Intelligence: " + str(Etrius.intelligenceScore))


#build an item
thingOnGround = gameItem.gameItem()
#thingOnGround.quickBuild()
thingOnGround.loadItemFromFile(open("./GameItems/ironsword.gmitm"))
print(thingOnGround.name)
print(thingOnGround.description)
print(thingOnGround.actions)

for action in thingOnGround.actions:
    action()

#add item to character inventory
Etrius.collectItem(thingOnGround) 
print(Etrius.inventory)


#make a new item and save it
newItem = gameItem.gameItem()
newItem.name = "SpellBook of Etrius"
newItem.description = "An ancient tome riddled with holy runes that holds divine insight."
newItem.actions = [gameItemActionDictionary.explode]
newItem.saveItemToFile()
"""



