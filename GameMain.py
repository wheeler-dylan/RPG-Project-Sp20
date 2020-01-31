#Author:        John P Armentor
#Date:          2019 01 30
#Course:        CSC242 - Software Engineering II
#Prof:         Dr. A. Louise Perkins

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
    
    # We create an ID using the network as an identifier for ourself
    #
    myAdventurerID = currentNetwork.getAdventurerID()

    # Main Game Loop
    #
    while run:
    
        # We get the ID of the other player's character
        #
        otherAdventurerID = currentNetwork.send(myAdventurerID)

        # We prompt the player to update what their character is thinking
        #
        myAdventurerID.think()
        
        # We call the Adventurer introduce method to demonstrate it works 
        #
        myAdventurerID.introduce()
        otherAdventurerID.introduce()
        
        # We have both characters speak their mind
        #
        myAdventurerID.speak()
        otherAdventurerID.speak()

main()