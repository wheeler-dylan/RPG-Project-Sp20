############################
# sandbox file for testing #
############################

import sys
sys.path.append('./player_character/')
sys.path.append('./player_character/abilities')
sys.path.append('./player_character/skills')
sys.path.append('./game_items')
sys.path.append('./game_engine')

import player_character
import character_creation
import abilities
import skills
import game_item
import game_item_actions
import user
import tabletop
import main_menu
import chat_message
import dice

import tkinter
import uuid


print("-------------------------Running sandbox.py-------------------------\n\n")

command = ""

player1 = player_character.PlayerCharacter()
user1 = user.Player()
user1.character.append(player1)
user1.active_character = user1.character[0]

gm1 = user.Player()
gm1.is_gamemaster = True

table1 = tabletop.Tabletop(gm1)
table1.put_on_table(user1)



instructions = ("\n\nsandbox commands:\n" +
                "exit:\tclose the program\n" +
                "help:\tprint list of commands\n" +
                #"AAAAAH!:\trun every command\n" +

                "\n----- Player Character Commands -----\n" +
                "create:\tcreate a new character with gui\n" +
                "abils:\toutput the character's abilities\n" +
                "skills:\toutput the character's skills\n" +
                "bags:\tview the character's inventory\n" +
                #"quick:\tinstantly create a basic character\n" +
                #"sheet:\toutput all the character's stats\n" +

                "\n----- Game Item Commands -----\n" +
                "look:\tview a list of all items in the game items folder\n" +
                "find:\tload some example items and add to inventory\n" +
                "craft:\tbuild a new item with gui\n" +

                "\n----- Game Engine Commands -----\n" +
                "printskills:\tview all skills in the skills.gameconfig file\n" +
                "printabils:\tview all abilities in the abilities.gameconfig file\n" +
                "table:\tplace the character and a new item on the table and confirm\n" +
                "main:\topen the main game window\n" +
                "roll:\tmake a quick dice check (non-skill based)\n" +

                "\n----- Chatlog -----\n" +
                "psst:\tput a chat message on the table and output to console\n" +
                "speak:\tspeak an inputted message and place in chat log\n" + 
                "walk:\tputs a walking action message into the chat log\n" +
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
        character_creation.character_creation(player1)
    
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
            print(str(each_skill.name)+":\t" + str(player1.skills[each_skill.id]))
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
        item_list = game_item.load_items_list()
        for each_item in item_list:
            print(each_item.name)
        print("\n-------------------------\n")

    #tests game item load and print
    elif (command == "find"):       
        print("-------------------------\n")
        ironSword = game_item.GameItem()
        ironSword.load_item_from_file(open("./game_items/ironsword.gmitm"))
        ironSword.print_item()
        player1.collect_item(ironSword)
        print("\n")
        journal = game_item.GameItem()
        journal.load_item_from_file(open("./game_items/journal.gmitm"))
        journal.print_item()
        player1.collect_item(journal)
        print("\n-------------------------\n")

    #tests GUI item creation
    elif (command == "craft"):      
        print("-------------------------\n")
        new_item = game_item.GameItem()
        game_item.game_item_creation(new_item)
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
        table1.put_on_table(player1) 

        some_item = game_item.GameItem()
        some_item.quick_build()
        print("\n")
        table1.put_on_table(some_item)
        
        for each_character in table1.player_characters.values():
            print(each_character.name) 

        for each_item in table1.game_items.values():
            print(each_item.name)

        print("\n-------------------------\n")

    #open main window
    elif (command == "main"):
        window = main_menu.MainMenu(table1, user1)
        window.mainloop()

    #make a non skill based check
    elif (command == "roll"):
        print("-------------------------\n")
        prob = input("Enter probability of success:")
        diff = input("Enter difficulty grade:")
        dice.roll_check(prob, diff)
        print("\n-------------------------\n")








    ##### Chatlog Commands #####
    
    #create a quick chat message and add to chatlog
    elif (command == "psst"):
        print("-------------------------\n")

        msg = chat_message.ChatMessage(player1, "speech", "public", "Hello World!")
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()

        print("\n-------------------------\n")

    #create a custom chat message and add to chatlog
    elif (command == "speak"):
        print("-------------------------\n")

        msg = chat_message.ChatMessage(player1, "speech", "public", 
                                       input("Enter your message..."))
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()

        print("\n-------------------------\n")


    #create an action message and add to chatlog
    elif (command == "walk"):
        print("-------------------------\n")

        msg = chat_message.ChatMessage(player1, "action", "public", 
                                       "walks forward " + str(player1.speed) + " feet.")
        table1.put_on_table(msg)
        table1.chatlog[msg.object_id].print_chat_message()

        print("\n-------------------------\n")

    #invalid command
    else:
        print("Command not valid, enter 'help' to view a list of commands.\n")

#end command switch
        






