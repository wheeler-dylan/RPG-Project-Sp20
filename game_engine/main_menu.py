#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 11
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class and methods for generating 
#   the main menu GUI from which all other menus will be opened
#   the vast majority of the game will occur here.


import sys
sys.path.append('./player_character/')
sys.path.append('./player_character/abilities')
sys.path.append('./player_character/skills')
sys.path.append('./game_items')

import player_character
import abilities
import skills
import game_item
import game_item_actions
import tabletop

import tkinter
import uuid


class MainMenu():
    def __init__(self, f_game_table, f_player):
        self.object_id = uuid.uuid1() 
        self.game_table = f_game_table
        self.player = f_player  #user who opens the game
    #end initializer


    #use tkinter to build main window
    def open_window(self):
        main_window = tkinter.Tk()
        main_window.title("Chatquest RPG")
        main_window.geometry("800x500")

        #populate chatlog
        chatlog_frame = tkinter.LabelFrame(main_window, text = "Chatlog:", padx = 5, pady = 5)
        chatlog_frame.pack()
        for each_message in self.game_table.chatlog.values():
            this_message = self.message_formatter(each_message, chatlog_frame)      #create formatted message
            this_message.pack()                                                     #add to chatlog

        main_window.mainloop()
    #end window


    #function to format the message text to be added to the chat log
    def message_formatter(self, f_message, f_frame):
        formatted_text = (str(f_message.speaker.name) + " says:\n" +
                          "\t" + f_message.message)
        msg = tkinter.Label(f_frame, text = formatted_text)
        return msg
    #



#end class