#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:  2020 02 10
#Course:    CSC425 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# Main game method of our project.

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
from functools import partial

from network import Network
import queue

# definition of Main
#
def main():

    # Set run to true to keep the game looping
    #
    run = True
    
    # We initialize a network object to communicate with the server
    #
    current_network = Network()
    function_queue = queue.Queue()
    
    gm1 = user.Player()
    gm1.is_gamemaster = True
    gm1.active_character = player_character.PlayerCharacter()
    gm1.active_character.name = "Gamemaster"


    table1 = tabletop.Tabletop(gm1)
    
    table1 = current_network.get_initial_data()
    

    # Main Game Loop
    #
    while run:
    
        synced_tabletop = current_network.send(function_queue)
        
main()