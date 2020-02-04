############################
# sandbox file for testing #
############################

import sys
sys.path.append('./PlayerCharacter')
import playerCharacter
sys.path.append('./GameItems')
import gameItem
import gameItemActionDictionary


print("-------------------------Running sandbox.py-------------------------\n\n")

command = ""
player1 = playerCharacter.playerCharacter()

while(command != "exit"):
    instructions = ("\n\nsandbox commands:\n" +
                    "exit:\tclose the program\n" +
                    "build:\tcreate a new character with gui\n" +
                    #"quick:\tcreate a basic character\n" +
                    "abils:\toutput the character's abilities\n" +
                    "skills:\toutput the character's skills\n" +
                    "sheet:\toutput all the character's stats\n\n\n")
    print(instructions)
    command = input()

    if (command == "build"):
        playerCharacter.characterCreation(player1)
    elif (command == "abils"):
        for eachScore in playerCharacter.coreAbilityScores:
            print(str(eachScore)+":\t"+str(player1.abilityScores[eachScore]))
    elif (command == "skills"):
        for eachSkill in playerCharacter.coreSkills:
            print(str(eachSkill[0])+"\t"+str(player1.skills[eachSkill[0]]))




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



