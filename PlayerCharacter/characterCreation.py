#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 06
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

import playerCharacter
import tkinter
import sys
sys.path.append('./PlayerCharacter/Skills')
import skills
sys.path.append('./PlayerCharacter/Abilities')
import abilities

#ability score parameters
minAbilityScore = 5                     #minimum score, starting score at initialization
startingAbilityPointsPerScore = 10      #this number defines the average points per score at character creation
startingAbilityPoints = startingAbilityPointsPerScore * len(abilities.coreAbilities)  #total of above
maxAbilityScore = 20                    #maximum ability score bonus at character creation


#skill rank parameters
minSkillRanks = 0                #minimum additional points added to each skill besides linked abilities
startingSkillPoints = 40        #total character creation points added to skill ranks
maxSkillRanks = 40              #maximux skill bonus allowed at character creation



###################################
#### character creation screen ####
###################################
def characterCreation(fCharacter):
        
    print("Character Creation:")
    print()
    
    #tkinter window for GUI character creation
    characterCreationWindow = tkinter.Tk() #character creation window
    characterCreationWindow.title("Character Creation")






    ############ Abilities ############

    #remaining points to spend on abilities
    abilityPointsLeft = startingAbilityPoints 
    #highest bonus to be added to ability scores
    abilityMaxBonus = min(maxAbilityScore - minAbilityScore, 
                          abilityPointsLeft)

    #dictionary used to be converted to list
    #   list will be used as parameters for the character object's
    #   update abilites function
    abilityBonuses = {}
    for eachAbility in abilities.coreAbilities.values():
        abilityBonuses[eachAbility.ID] = 0


    #give instructions for adding points to ability scores
    abilityBanner = str("Abilities:\nYou have " + str(abilityPointsLeft) + 
                        " points to distribute amongst your ability scores.\n" + 
                        "Each score starts at " + str(minAbilityScore) + ".\n" +
                        "The maximum for each score is " + str(maxAbilityScore) + ".")
    label = tkinter.Label(text = abilityBanner).pack()


    #used when the ability score spinbox arrows are clicked, 
    #   updates the bonuses with new value from the spinbox
    def abilitySpinboxUpdate():
        #update ability bonuses based off values in the spinboxes
        for eachAbility in abilities.coreAbilities.values():
            abilityBonuses[eachAbility.ID] = int(abilityBonusSpinboxes[eachAbility.ID].get()) 

        #check how many points are left
        abilityBonusSum = 0
        for eachAbility in abilities.coreAbilities.values():
            abilityBonusSum += abilityBonuses[eachAbility.ID]
        abilityPointsLeft = startingAbilityPoints - abilityBonusSum
        abilityMaxBonus = maxAbilityScore - minAbilityScore 

        #don't let player spend more points than they have, resets spinbox max values
        if(abilityPointsLeft == 0):
            for eachAbility in abilities.coreAbilities.values():
                abilityBonusSpinboxes[eachAbility.ID].config(to = int(abilityBonusSpinboxes[eachAbility.ID].get()))

        #reset maximums if player deallocates points or has points left
        else:
            for eachAbility in abilities.coreAbilities.values():
                abilityBonusSpinboxes[eachAbility.ID].config(
                    to = min(abilityMaxBonus, 
                             int(abilityBonusSpinboxes[eachAbility.ID].get()) + 
                             abilityPointsLeft))

        #debugging
        #print(abilityBonuses, end="\t")
        #print(abilityPointsLeft, abilityMaxBonus)
    #end ability spinbox update
    
    #add a spinbox user uses to allocate points to each ability score
    abilityBonusSpinboxes = {}
    for eachAbility in abilities.coreAbilities.values():
        label = tkinter.Label(text = eachAbility.name + ":").pack() 
        abilityBonusSpinboxes[eachAbility.ID] = tkinter.Spinbox(
            characterCreationWindow, from_ = 0, to = abilityMaxBonus, 
            command = abilitySpinboxUpdate)
        abilityBonusSpinboxes[eachAbility.ID].pack()
    #
    label = tkinter.Label(text="").pack() #blank line

    ###################################






    ############ Skills ############

    #remaining points to spend on skills
    skillPointsLeft = startingSkillPoints
    #highest bonus that can be added to skill ranks
    skillMaxBonus = min(maxSkillRanks - minSkillRanks, skillPointsLeft)

    #dictionary used to be converted to list
    #   list will be used as parameters for the character object's
    #   update abilites function
    skillBonuses = {}
    for eachSkill in skills.coreSkills.values():
        skillBonuses[eachSkill.ID] = 0


    #give instructions for adding points to skill ranks
    skillBanner = str("Skills:\nYou have " + str(skillPointsLeft) + " "+ 
                      "points to distribute amongst your skill ranks.\n" + 
                      "Each rank starts at " + str(minSkillRanks) + ".\n" +
                      "The maximum for each rank is " + str(maxSkillRanks) + ".\n" +
                      "In addition to ranks, each skill gains a bonus from " +
                      "each of its two link Abilities.")
    label = tkinter.Label(text = skillBanner).pack()


    #update skill bonuses when skill spinbox arrows are clicked
    def skillSpinboxUpdate():
        #update skill bonuses based off values in the spinboxes
        for eachSkill in skills.coreSkills.values():
            #if (int(skillBonusSpinboxes[eachSkill[0]].get()) > int(maxSkillRanks)):   #input validation
            #    skillBonusSpinboxes[eachSkill[0]].set(int(maxSkillRanks))
            skillBonuses[eachSkill.ID] = int(skillBonusSpinboxes[eachSkill.ID].get())

        #check how many points are left for skills
        skillBonusSum = 0
        for eachSkill in skills.coreSkills.values():
            skillBonusSum += skillBonuses[eachSkill.ID]
        skillPointsLeft = startingSkillPoints - skillBonusSum

        #don't let player spend more points than they have, reset spinbox max values
        """
        if(skillPointsLeft == 0):
            for eachSkill in playerCharacter.coreSkills:
                skillBonusSpinboxes[eachSkill[0]].config(
                    to = int(skillBonusSpinboxes[eachSkill[0]].get()))
        else:
            for eachSkill in playerCharacter.coreSkills:
                skillBonusSpinboxes[eachSkill[0]].config(
                    to = min(skillMaxBonus, 
                             int(skillBonusSpinboxes[eachSkill[0]].get()) + skillPointsLeft))
        """
        for eachSkill in skills.coreSkills.values():
            skillBonusSpinboxes[eachSkill.ID].config(
                to = min(skillMaxBonus, 
                         int(skillBonusSpinboxes[eachSkill.ID].get()) + skillPointsLeft))


    #end skill spinbox update

    #add a spinbox user uses to allocate points to each skill rank
    skillBonusSpinboxes = {}
    for eachSkill in skills.coreSkills.values():
        label = tkinter.Label(text = str(eachSkill.name) + " (" +
                              str(eachSkill.mainAbility) + ", " +
                              str(eachSkill.secondaryAbility) + "):").pack()
        skillBonusSpinboxes[eachSkill.ID] = tkinter.Spinbox(characterCreationWindow, from_ = 0, 
                                                            to = maxSkillRanks,
                                                            command = skillSpinboxUpdate)
        skillBonusSpinboxes[eachSkill.ID].pack()
    #
    label = tkinter.Label(text="").pack() #blank line
    
    ###################################




    characterCreationWindow.mainloop()
    #end character creation window
        
    #debugging
    #print(abilityBonuses)





    #update scores
    newAbilityScores = []
    for eachAbility in abilities.coreAbilities.values():
        newAbilityScores.append(abilityBonuses[eachAbility.ID])
    fCharacter.updateAbilityScores(newAbilityScores)

    newSkillRanks = []
    for eachSkill in skills.coreSkills.values():
        newSkillRanks.append(skillBonuses[eachSkill.ID])
    fCharacter.updateSkillRanks(newSkillRanks)

#end character creation function
