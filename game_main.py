#Author:        John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:      2020 02 10
#Course:        CSC424 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# Main game method of our project.

from network import Network
from adventurer import Adventurer

# definition of Main
#
def main():

    # Set run to true to keep the game looping
    #
    run = True
    
    # We initialize a network object to communicate with the server
    #
    current_network = Network()
    
    game_objects = current_network.get_client_id()

    # Main Game Loop
    #
    while run:
    
        game_objects = current_network.send(game_objects)
        
        for i in game_objects:
            i.introduce()
            i.speak()
        
        name = input("Name.")
        tmp = Adventurer(name, "Peasant", 10, "work work")
        
        game_objects.append(tmp)
        
        
main()