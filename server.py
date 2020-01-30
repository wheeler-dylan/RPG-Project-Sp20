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


adventurers = [Adventurer("Jack", "Bandit", 10, "Hello!"), Adventurer("Jill", "Bandit", 10, "Hello!")]

def threaded_client(conn, adventurer):
    conn.send(pickle.dumps(adventurers[adventurer]))
    reply = ""
    while True:
        try:
            inboundData = pickle.loads(conn.recv(2048))
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

            conn.sendall(pickle.dumps(outboundData))
        except:
            break

    print("Lost connection")
    conn.close()

currentAdventurerCount = 0
while True:
    conn, addr = currentSocket.accept()
    print("Connected established with:", addr)

    start_new_thread(threaded_client, (conn, currentAdventurerCount))
    currentAdventurerCount += 1