#Author:        John P Armentor
#Date:          2019 01 30
#Course:        CSC242 - Software Engineering II
#Prof:         Dr. A. Louise Perkins

# File for the object that acts as the network for our game.  Allows the
# sending of serialized objects to the server as well as for obtaining the player's ID

import socket
import pickle
from settings import *

# The class we initialize to interact with the server
#
class Network:
    def __init__(self):
    
        # We establish a socket with the type of connection will will be using.
        # AF_INET showing that we are using IPv4 and SOCK_STREAM showing
        # it is a TCP socket
        #
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # The server IP we will pull from our settings.py file
        #
        self.server = LOCALHOST
        
        # a good, typically open port, but can be changed as needed
        #
        self.port = 5555
        
        # we create our address 
        #
        self.address = (self.server, self.port)
        
        # we create an ID that we can use to easily identify our connection
        #
        self.adventurerID = self.connect()

    def getAdventurerID(self):
        return self.adventurerID

    # our function to attempt to connect to the server 
    #
    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    # we using pickling to serialize objects and send data to the server as needed
    #
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error:
            print(socket.error)
