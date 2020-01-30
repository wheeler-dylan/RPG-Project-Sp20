from network import Network
from adventurer import Adventurer

def main():
    run = True
    currentNetwork = Network()
    myAdventurerID = currentNetwork.getAdventurerID()

    while run:
        otherAdventurerID = currentNetwork.send(myAdventurerID)

        myAdventurerID.think()
        myAdventurerID.speak()
        otherAdventurerID.speak()

main()