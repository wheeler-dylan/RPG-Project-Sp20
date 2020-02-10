#Author:        John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:      2020 02 10
#Course:        CSC424 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# File that acts as the server for our game.  Intended to be launchable by
# anyone looking to host.

import socket
import pickle
from _thread import *
from network import Network
from adventurer import Adventurer
from settings import *

# We create a function that acts as a threaded client that accepts the connection as an object and additionally accepts an object
# that is to be pickled and transfered, which is the Game objects in this case
#
def threaded_client(connection, gameObjects):
    connection.send(pickle.dumps(gameObjects))
    reply = ""
    while True:
        try:
            
            # we attempt to recieve 2048 bits of data that was pickled and we can increase the size of the data using the multiplier
            #
            inboundData = pickle.loads(connection.recv(2048*20))
            print("Incoming: ", inboundData)
            
            gameObjects = inboundData

            # this is to show that we are disconnecting and the break out once the client stops sending information and loses connection
            #
            if not inboundData:
                print("Disconnected")
                break
                
            # else we send back the updated list of gameObjects
            #            
            else:
                outboundData = gameObjects
                connection.sendall(pickle.dumps(outboundData))
                print("Outgoing : ", outboundData)
                    
        except:
            break
            
    # To cover the case of the connection closing to prevent any infinite loops 
    #
    print("Lost connection")
    connection.close()

# We set a variable for the server the same as our local host setting in out settings.py file
#
server = LOCALHOST

# We set the port to 5555 as it is in a commonly unused port range to avoid the commonly used ones
#
port = 5555

# We now create a socket and use the settings to show that we are using TCP (SOCK_STREAM) and IPv4 (AF_INET)
#
currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# a try except in the even that an error is thrown when we attempt to bind to the server and port
# useful if the port is in use
#
try:
    currentSocket.bind((server, port))
except socket.error:
    str(socket.error)

# We listen for 6 total connections, limiting how many can connect to the server, this dictates the server size limit
#
currentSocket.listen(6)
print("--Server Initialized--")
print("Listening for Connections...")

# We create a list of Game objects to track and store all game-related information from the clients to the server, and then
# transmit that information back to the clients.
#
gameObjects = [Adventurer("Chronos", "Diety", 1, "I am")]

# we create a loop that constantly checks for new connections to be accepted and establishes a threaded client connection
#
while True:
    connection, address = currentSocket.accept()
    print("Connected established with:", address)

    start_new_thread(threaded_client, (connection, gameObjects))