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
    currentNetwork = Network()
    
    gameObjects = currentNetwork.getClientID()

    # Main Game Loop
    #
    while run:
    
        gameObjects = currentNetwork.send(gameObjects)
        
        for i in gameObjects:
            i.introduce()
            i.speak()
        
        name = input("Name.")
        tmp = Adventurer(name, "Peasant", 10, "work work")
        
        gameObjects.append(tmp)
        
        
main()