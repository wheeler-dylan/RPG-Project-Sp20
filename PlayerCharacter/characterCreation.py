

import playerCharacter
import tkinter

#ability score parameters
minAbilityScore = 5                     #minimum score, starting score at initialization
startingAbilityPointsPerScore = 10      #this number defines the average points per score at character creation
startingAbilityPoints = startingAbilityPointsPerScore * len(playerCharacter.coreAbilityScores)  #total of above
maxAbilityScore = 20                    #maximum ability score bonus at character creation


#skill rank parameters
minSkillRank = 0                #minimum additional points added to each skill besides linked abilities
startingSkillPoints = 40        #total character creation points added to skill ranks
maxSkillRanks = 40              #maximux skill bonus allowed at character creation



###################################
#### character creation screen ####
###################################
def characterCreation(fCharacter):
        
    print("Character Creation:")
    print()
    
    #tkinter window for GUI character creation
    ccWindow = tkinter.Tk() #character creation window
    ccWindow.title("Character Creation")






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
    for eachScore in playerCharacter.coreAbilityScores:
        abilityBonuses[eachScore] = 0


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
        for eachScore in playerCharacter.coreAbilityScores:
            abilityBonuses[eachScore] = int(abilityBonusSpinboxes[eachScore].get()) 

        #check how many points are left
        abilityBonusSum = 0
        for eachScore in playerCharacter.coreAbilityScores:
            abilityBonusSum += abilityBonuses[eachScore]
        abilityPointsLeft = startingAbilityPoints - abilityBonusSum
        abilityMaxBonus = maxAbilityScore - minAbilityScore 

        #don't let player spend more points than they have, resets spinbox max values
        if(abilityPointsLeft == 0):
            for eachScore in playerCharacter.coreAbilityScores:
                abilityBonusSpinboxes[eachScore].config(to = int(abilityBonusSpinboxes[eachScore].get()))

        #reset maximums if player deallocates points or has points left
        else:
            for eachScore in playerCharacter.coreAbilityScores:
                abilityBonusSpinboxes[eachScore].config(
                    to = min(abilityMaxBonus, int(abilityBonusSpinboxes[eachScore].get()) + abilityPointsLeft))

        #debugging
        print(abilityBonuses, end="\t")
        print(abilityPointsLeft, abilityMaxBonus)
    #end ability spinbox update
    
    #add a spinbox user uses to allocate points to each ability score
    abilityBonusSpinboxes = {}
    for eachScore in playerCharacter.coreAbilityScores:
        label = tkinter.Label(text = eachScore.capitalize() + ":").pack() 
        abilityBonusSpinboxes[eachScore] = tkinter.Spinbox(ccWindow, from_ = 0, to = abilityMaxBonus, 
                                                           command = abilitySpinboxUpdate)
        abilityBonusSpinboxes[eachScore].pack()
    #
    label = tkinter.Label(text="").pack() #blank line

    ###################################






    ############ Skills ############

    #remaining points to spend on skills
    skillPointsLeft = startingSkillPoints
    #highest bonus that can be added to skill ranks
    skillMaxBonus = min(maxSkillRanks - minSkillRank, skillPointsLeft)

    #dictionary used to be converted to list
    #   list will be used as parameters for the character object's
    #   update abilites function
    skillBonuses = {}
    for eachSkill in playerCharacter.coreSkills:
        skillBonuses[eachSkill[0]] = 0


    #give instructions for adding points to skill ranks
    skillBanner = str("Skills:")        #TODO
    label = tkinter.Label(text = skillBanner).pack()


    #update skill bonuses when skill spinbox arrows are clicked
    def skillSpinboxUpdate():
        #update skill bonuses based off values in the spinboxes
        for eachSkill in playerCharacter.coreSkills:
            #if (int(skillBonusSpinboxes[eachSkill[0]].get()) > int(maxSkillRanks)):   #input validation
            #    skillBonusSpinboxes[eachSkill[0]].set(int(maxSkillRanks))
            skillBonuses[eachSkill[0]] = int(skillBonusSpinboxes[eachSkill[0]].get())

        #check how many points are left for skills
        skillBonusSum = 0
        for eachSkill in playerCharacter.coreSkills:
            skillBonusSum += skillBonuses[eachSkill[0]]
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
        for eachSkill in playerCharacter.coreSkills:
            skillBonusSpinboxes[eachSkill[0]].config(
                to = min(skillMaxBonus, 
                         int(skillBonusSpinboxes[eachSkill[0]].get()) + skillPointsLeft))


    #end skill spinbox update

    #add a spinbox user uses to allocate points to each skill rank
    skillBonusSpinboxes = {}
    for eachSkill in playerCharacter.coreSkills:
        label = tkinter.Label(text = eachSkill[0].capitalize() + " (" +
                              eachSkill[1].capitalize() + ", " +
                              eachSkill[2].capitalize() + "):").pack()
        skillBonusSpinboxes[eachSkill[0]] = tkinter.Spinbox(ccWindow, from_ = 0, to = maxSkillRanks,
                                                           command = skillSpinboxUpdate)
        skillBonusSpinboxes[eachSkill[0]].pack()
    #
    label = tkinter.Label(text="").pack() #blank line
    
    ###################################




    ccWindow.mainloop()
    #end character creation window
        
    #debugging
    print(abilityBonuses)





    #update scores
    newAbilityScores = []
    for eachScore in playerCharacter.coreAbilityScores:
        newAbilityScores.append(abilityBonuses[eachScore])
    fCharacter.updateAbilityScores(newAbilityScores)

    newSkillRanks = []
    for eachSkill in playerCharacter.coreSkills:
        newSkillRanks.append(skillBonuses[eachSkill[0]])
    fCharacter.updateSkillRanks(newSkillRanks)

#end character creation function
