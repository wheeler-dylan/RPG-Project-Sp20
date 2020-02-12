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
sys.path.append('./PlayerCharacter/Skills')
import skills
sys.path.append('./PlayerCharacter/Abilities')
import abilities
sys.path.append('./GameState')
import tabletop


print("-------------------------Running sandbox.py-------------------------\n\n")

command = ""
player1 = playerCharacter.playerCharacter()
game_table = tabletop.tabletop()




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

                "\n----- Game Engine Commands -----\n" +
                "printskills:\tview all skills in the skills.gameconfig file\n" +
                "printabils:\tview all abilities in the abilities.gameconfig file\n" +
                "table:\tplace the character on the table and confirm\n" +
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


    ##### PC Commands #####

    #tests Character Creation GUI
    elif (command == "create"):     
        characterCreation.character_creation(player1)
    
    #ensures ability scores have been updated
    elif (command == "abils"):      
        print("-------------------------\n")
        for each_ability in abilities.core_abilities.values():
            print(str(each_ability.name)+":\t" + 
                  str(player1.ability_scores[each_ability.id]))
        print("\n-------------------------\n")

    #ensures skills have been updated
    elif (command == "skills"):     
        print("-------------------------\n")
        for each_skill in skills.core_skills.values():
            print(str(each_skill.name)+":\t"+str(player1.skills[each_skill.id]))
        print("\n-------------------------\n")

    #view characters inventory
    elif (command == "bags"):       
        print("-------------------------\n")
        for each_item in player1.inventory:
            print(each_item.name)
        print("\n-------------------------\n")


    ##### Game Item Commands #####

    #tests function to get a list of game items from folder
    elif (command == "look"):       
        print("-------------------------\n")
        item_list = gameItem.load_items_list()
        for each_item in item_list:
            print(each_item.name)
        print("\n-------------------------\n")

    #tests game item load and print
    elif (command == "find"):       
        print("-------------------------\n")
        ironSword = gameItem.game_item()
        ironSword.load_item_from_file(open("./GameItems/ironsword.gmitm"))
        ironSword.print_item()
        player1.collect_item(ironSword)
        print("\n")
        journal = gameItem.game_item()
        journal.load_item_from_file(open("./GameItems/journal.gmitm"))
        journal.print_item()
        player1.collect_item(journal)
        print("\n-------------------------\n")

    #tests GUI item creation
    elif (command == "craft"):      
        print("-------------------------\n")
        new_item = gameItem.game_item()
        gameItem.game_item_creation(new_item)
        new_item.print_item()
        player1.collect_item(new_item) #add to inventory
        print("\n-------------------------\n")


    ##### Game Engine Commands #####

    #confirm skills loaded from game config file
    elif (command == "printskills"):
        print("-------------------------\n")
        for each_skill in skills.core_skills.values():
            each_skill.print_skill()
            print("\n----------\n")
        print("\n-------------------------\n")

    #confirm skills loaded from game config file
    elif (command == "printabils"):
        print("-------------------------\n")
        for each_ability in abilities.core_abilities.values():
            each_ability.print_ability()
            print("\n----------\n")
        print("\n-------------------------\n")

    #put the PC on the table
    elif (command == "table"):
        print("-------------------------\n")
        temp_pcuuid = "123456"       #use until a uid has been added to pc class
        game_table.put_on_table(temp_pcuuid, player1) 

        temp_giuuid = "654321"
        some_item = gameItem.gameItem()
        some_item.quickBuild()
        game_table.put_on_table(temp_giuuid, some_item)
        
        for each_character in game_table.player_characters.values():
            print(each_character.name) 

        for each_item in game_table.game_items.values():
            print(each_item.name)

        print("\n-------------------------\n")


    #invalid command
    else:
        print("Command not valid, enter 'help' to view a list of commands.\n")

#end command switch
        



