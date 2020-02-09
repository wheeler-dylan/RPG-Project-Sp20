#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 02
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#this file contains species playabel by player characters

class species: 
    def __init__(self, fName):
        self.name = fName

        #possible target zones, 
        #   dictionary with string key value for each tragetable body part
        #   paired with a percentage (0 to 100) representing the odds that 
        #   that area is hit. This would typically coorespond to the size
        #   of the area, so it also represents a portion of the hit points
        #   that area contains
        self.hitboxes = {}

        self.nativeLanguages = []

#end species definition

#list of all species
speciesList = {}

#list of all languages
languages = {"vernacular": "vernacular"}

#the human species
human = species("human")
human.hitboxes["head"] = 10
human.hitboxes["chest"] = 20
human.hitboxes["abdomen"] = 20
human.hitboxes["leftArm"] = 15
human.hitboxes["rightArm"] = 15
human.hitboxes["leftLeg"] = 10
human.hitboxes["rightLeg"] = 10
human.nativeLanguages.append(languages["vernacular"])
speciesList["human"] = human


