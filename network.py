import socket
import pickle
from settings import *


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = LOCALHOST
        self.port = 5555
        self.addr = (self.server, self.port)
        self.adventurerID = self.connect()

    def getAdventurerID(self):
        return self.adventurerID

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error:
            print(socket.error)
