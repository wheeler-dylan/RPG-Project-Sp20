import sys
sys.path.append('./PlayerCharacter')
import playerCharacter


print("-------------------------Running sandbox.py-------------------------\n\n")


#create new PC
Etrius = playerCharacter.playerCharacter()
Etrius.characterCreation()

#display scores
print("Strength: " + str(Etrius.strengthScore))
print("Constitution: " + str(Etrius.constitutionScore))
print("Dexterity: " + str(Etrius.dexterityScore))
print("Intelligence: " + str(Etrius.intelligenceScore))


