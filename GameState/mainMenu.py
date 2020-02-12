#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 11
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class and methods for generating 
#   the main menu GUI from which all other menus will be opened
#   the vast majority of the game will occur here.


import sys
sys.path.append('./PlayerCharacter/')
sys.path.append('./PlayerCharacter/Abilities')
sys.path.append('./PlayerCharacter/Skills')
sys.path.append('./GameItems')

import playerCharacter
import abilities
import skills
import gameItem
import gameItemActionDictionary

import tkinter
import uuid


class main_menu():
    def __init__(self):
        self.object_id = uuid.uuid1() 

    #end initializer