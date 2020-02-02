import sys
sys.path.append('./PlayerCharacter')
import playerCharacter
sys.path.append('./GameItems')
import gameItem
import gameItemActionDictionary


print("-------------------------Running sandbox.py-------------------------\n\n")


#create new PC
Etrius = playerCharacter.playerCharacter()
Etrius.characterCreation()

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



