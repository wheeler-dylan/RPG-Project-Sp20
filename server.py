#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Modified:      2020 02 10
#Course:    CSC425 - Software Engineering II
#Prof:      Dr. A. Louise Perkins

# File that acts as the server for our game.  Intended to be launchable by
# anyone looking to host.

import socket
import pickle
from _thread import *
from network import Network
from adventurer import Adventurer
from settings import *

# We create a list of Game objects to track and store all game-related information from the clients to the server, and then
# transmit that information back to the clients.
#
game_objects = [Adventurer("Chronos", "Diety", 1, "I am")]

# We create a function that acts as a threaded client that accepts the connection as an object and additionally accepts an object
# that is to be pickled and transfered, which is the Game objects in this case
#
def threaded_client(connection):

    # Uses the gameObjects list as a global variable so we can still employ multi-threading for the multiple clients
    #
    global game_objects

    connection.send(pickle.dumps(game_objects))
    while True:
        try:
            
            # we attempt to recieve 2048 bits of data that was pickled and we can increase the size of the data using the multiplier
            #
            inbound_data = pickle.loads(connection.recv(1024*4))
            print("Incoming: ", inbound_data)
            
            game_objects = inbound_data

            # this is to show that we are disconnecting and the break out once the client stops sending information and loses connection
            #
            if not inbound_data:
                print("Disconnected")
                break
                
            # else we send back the updated list of gameObjects
            #            
            else:
                outbound_data = game_objects
                connection.sendall(pickle.dumps(outbound_data))
                print("Outgoing : ", outbound_data)
                    
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
current_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# a try except in the even that an error is thrown when we attempt to bind to the server and port
# useful if the port is in use
#
try:
    current_socket.bind((server, port))
except socket.error:
    str(socket.error)

# We listen for connections, this can accept an integer, limiting how many can connect to the server, this dictates the server size limit
#
current_socket.listen()
print("--Server Initialized--")
print("Listening for Connections...")

# we create a loop that constantly checks for new connections to be accepted and establishes a threaded client connection
#
while True:
    connection, address = current_socket.accept()
    print("Connected established with:", address)

    start_new_thread(threaded_client, (connection,))