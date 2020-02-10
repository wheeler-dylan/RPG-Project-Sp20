#Author:        John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:      2020 02 09
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
    
    # We create an ID using the network as an identifier for ourself
    #
    myClientID = currentNetwork.getClientID()
    
    gameObjects = [Adventurer("Chronos", "Diety", 1, "I am")]
    objectExists = False

    # Main Game Loop
    #
    while run:
        for i in gameObjects:
            currentNetwork.send(i)
            
        inboundData = currentNetwork.recieve()

        for i in gameObjects:
            if(i.getObjectID() == inboundData.getObjectID()):
                i = inboundData
                objectExists = True
                break

            if objectExists == False:
                gameObjects.append(inboundData)

            objectExists = False
        
        for i in gameObjects:
            i.introduce()
            i.speak()


main()