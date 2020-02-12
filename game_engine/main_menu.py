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

import tkinter
import uuid


class MainMenu():
    def __init__(self):
        self.object_id = uuid.uuid1() 

    #end initializer

#end class