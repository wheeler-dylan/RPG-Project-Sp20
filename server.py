#Author:        John P Armentor
#Date:          2019 01 30
#Course:        CSC242 - Software Engineering II
#Prof:         Dr. A. Louise Perkins

# File that acts as the server for our game.  Intended to be launchable by
# anyone looking to host.

import socket
import pickle
from _thread import *
from network import Network
from adventurer import Adventurer
from settings import *

server = LOCALHOST
port = 5555

currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    currentSocket.bind((server, port))
except socket.error:
    str(socket.error)

currentSocket.listen(2)
print("--Server Initialized--")
print("Listening for Connections...")


adventurers = [Adventurer("Jack", "Bandit", 10, "Hello!"), Adventurer("Jill", "Mage", 10, "Hello!")]

def threaded_client(connection, adventurer):
    connection.send(pickle.dumps(adventurers[adventurer]))
    reply = ""
    while True:
        try:
            inboundData = pickle.loads(connection.recv(2048))
            adventurers[adventurer] = inboundData

            if not inboundData:
                print("Disconnected")
                break
            else:
                if adventurer == 1:
                    outboundData = adventurers[0]
                else:
                    outboundData = adventurers[1]

                print("Incoming: ", inboundData)
                print("Outgoing : ", outboundData)

            connection.sendall(pickle.dumps(outboundData))
        except:
            break

    print("Lost connection")
    connection.close()

currentAdventurerCount = 0
while True:
    connection, address = currentSocket.accept()
    print("Connected established with:", address)

    start_new_thread(threaded_client, (connection, currentAdventurerCount))
    currentAdventurerCount += 1