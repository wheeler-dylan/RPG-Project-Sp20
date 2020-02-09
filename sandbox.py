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
                "create:\tcreate a new character with gui\n" +
                #"quick:\tinstantly create a basic character\n" +
                "abils:\toutput the character's abilities\n" +
                "skills:\toutput the character's skills\n" +
                "bags:\tview the character's inventory\n" +
                #"sheet:\toutput all the character's stats\n" +

                "\n----- Game Item Commands -----\n" +
                "look:\tview a list of all items in the game items folder\n" +
                "find:\tload some example items and add to inventory\n" +
                "craft:\tbuild a new item with gui\n" +
                "\n")
print(instructions)



while(command != "exit"):
    command = input()

    #input command switch
    if (command == "exit"):
        break

    #output valid commands for sandbox
    elif (command == "help"):         
        print("-------------------------\n")
        print(instructions)
        print("\n-------------------------\n")

    #tests Character Creation GUI
    elif (command == "create"):     
        characterCreation.characterCreation(player1)
    
    #ensures ability scores have been updated
    elif (command == "abils"):      
        print("-------------------------\n")
        for eachScore in playerCharacter.coreAbilityScores:
            print(str(eachScore)+":\t"+str(player1.abilityScores[eachScore]))
        print("\n-------------------------\n")

    #ensures skills have been updated
    elif (command == "skills"):     
        print("-------------------------\n")
        for eachSkill in playerCharacter.coreSkills:
            print(str(eachSkill[0])+"\t"+str(player1.skills[eachSkill[0]]))
        print("\n-------------------------\n")

    #view characters inventory
    elif (command == "bags"):       
        print("-------------------------\n")
        for eachItem in player1.inventory:
            print(eachItem.name)
        print("\n-------------------------\n")

    #tests function to get a list of game items from folder
    elif (command == "look"):       
        print("-------------------------\n")
        itemList = gameItem.loadItemsList()
        for eachItem in itemList:
            print(eachItem.name)
        print("\n-------------------------\n")

    #tests game item load and print
    elif (command == "find"):       
        print("-------------------------\n")
        ironSword = gameItem.gameItem()
        ironSword.loadItemFromFile(open("./GameItems/ironsword.gmitm"))
        ironSword.printItem()
        player1.collectItem(ironSword)
        print("\n")
        journal = gameItem.gameItem()
        journal.loadItemFromFile(open("./GameItems/journal.gmitm"))
        journal.printItem()
        player1.collectItem(journal)
        print("\n-------------------------\n")

    #tests GUI item creation
    elif (command == "craft"):      
        print("-------------------------\n")
        newItem = gameItem.gameItem()
        gameItem.gameItemCreation(newItem)
        newItem.printItem()
        player1.collectItem(newItem) #add to inventory
        print("\n-------------------------\n")

    #invalid command
    else:
        print("Command not valid, enter 'help' to view a list of commands.\n")

#end command switch
        



