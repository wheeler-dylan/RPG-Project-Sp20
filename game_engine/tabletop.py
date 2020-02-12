#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 11
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This class will act as the game state of a game station. 
#   "tabletop" refers to the game objects that are "in play",
#   and should be able to be refered to from anywhere in the program.
#
#   It will hold things like the players that are connected to 
#       the session and their characters, and any objects the 
#       Game Master (GM) wants to present to the players.

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

import tkinter
import uuid

#tabletop contains:
#   player characters
#   non player characters
#   game items

class Tabletop:
    def __init__(self):
        self.gamemaster_id = ""     #stores unique identifier of game master
        
        #store characters
        self.player_characters = {}         #controlled by players (remote users)
        self.nonplayer_characters = {}      #controlled by GM
        
        #store game items
        self.game_items = {}

        #store chatlog messages
        self.chatlog = {}

        #store anything that doesn't match a predefined class,
        #   used when put_on_table can't find the object's class type
        self.trunk = {}
    #end initializer
    
       
    #auto add to table function, determines the class type and stores in proper dictionary
    def put_on_table(self, f_token):
        if f_token.__class__.__name__ == "PlayerCharacter":
            self.player_characters[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "NonplayerCharacter":
            self.nonplayer_characters[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "GameItem":
            self.game_items[f_token.object_id] = f_token

        elif f_token.__class__.__name__ == "ChatMessage":
            self.chatlog[f_token.object_id] = f_token

        else:
            self.trunk[f_token.object_id] = f_token
    #


#end tabletop class
