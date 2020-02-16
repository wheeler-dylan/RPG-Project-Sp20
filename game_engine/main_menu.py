#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 11
#Course:        CSC425 - Software Engineering II
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
import chat_message

import tkinter
import uuid


class MainMenu(tkinter.Tk):
    def __init__(self, f_game_table, f_player):
        tkinter.Tk.__init__(self)
        self.object_id = uuid.uuid1() 
        self.game_table = f_game_table
        self.player = f_player
    
        self.title("Chatquest RPG")
        self.geometry("800x500")
        
        


        ##### CHAT ##### 
        #build frame
        self.chatlog_frame = tkinter.LabelFrame(self, text = "Chatlog:", padx = 5, pady = 5)
        self.chatlog_frame.pack(fill = "y")
        self.refresh_chatlog() #keep up to date

        for each_message in self.game_table.chatlog.values():
            #create formatted message
            this_message = self.message_formatter(each_message, self.chatlog_frame)      
            this_message.pack()
        #end populate chatlog

        #text entry to create chat message
        self.chat_entry = tkinter.Entry(self)     #text entry field
        self.chat_entry.pack()


        self.chat_submit = tkinter.Button(self, text = "Send", command = self.send_chat_message)
        self.chat_submit.pack()
        #end text entry chat message

        ##### END CHAT #####



        ##### HITPOINTS #####
        
        #output current HP
        #build frame
        self.hitpoint_frame = tkinter.LabelFrame(self, text = "Hitpoints:", 
                                              padx = 5, pady = 5)
        self.hitpoint_frame.pack()

        #get hitpoint maximums from player's character
        for each_hitbox in self.player.active_character.max_hitpoints:  
            hitpoint_string = (str(each_hitbox) + ": " +
                               str(self.player.active_character.current_hitpoints[each_hitbox]) +
                               "/" +
                               str(self.player.active_character.current_hitpoints[each_hitbox]) )
            
            hitpoint_label = tkinter.Label(self.hitpoint_frame, text = hitpoint_string)
            hitpoint_label.pack()

        ##### END HITPOINTS #####


    #end window






    #function to format the message text to be added to the chat log
    def message_formatter(self, f_message, f_frame):
        
        if (f_message.type == "speech"):        
            formatted_text = (str(f_message.speaker.name) + " says:\n" +
                              "\t" + str(f_message.message))
            msg = tkinter.Label(f_frame, text = formatted_text, foreground = "green")

        elif(f_message.type == "action"):
            formatted_text = (str(f_message.speaker.name) + " " + 
                              str(f_message.message))
            msg = tkinter.Label(f_frame, text = formatted_text, foreground = "red")

        elif (f_message.type == "technical"):
            msg = tkinter.Label(f_frame, text = f_message.message)

        return msg
    #


    #controller for chat entry send button
    def send_chat_message(self):
        if (len(self.chat_entry.get()) > 0):
            msg = chat_message.ChatMessage(self.player.active_character, 
                                           "speech", "public", 
                                           self.chat_entry.get())
            self.game_table.put_on_table(msg)
            self.game_table.chatlog[msg.object_id].print_chat_message()  #debugging
        self.chat_entry.delete(0, "end")        #clear the entry field
        #self.refresh_chatlog()

    #


    #refresh the chatlog
    def refresh_chatlog(self):
        for each_message in self.chatlog_frame.winfo_children():
            each_message.destroy()

        for each_message in self.game_table.chatlog.values():
            this_message = self.message_formatter(each_message, self.chatlog_frame)
            this_message.pack()

        self.after(250, self.refresh_chatlog)   #refresh 4 times per second
    #end refresh chatlog




#end class