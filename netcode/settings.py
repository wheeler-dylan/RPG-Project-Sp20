#Author:    John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 01 30
#Course:    CSC424 - Software Engineering II
#Prof:      Dr. A. Louise Perkins
#
#File for designating settings intended across the entire game.

import socket  

# Multiplayer settings
#
LOCALHOST = ""
MEMORYMULTIPLIER = 10

def setIP():
    selection = input("Enter 1 to host or 2 to join a server: ")
    
    if selection == 1:
        LOCALHOST = socket.gethostbyname(socket.gethostname())
        
    elif selection = 2:
        LOCALHOST = input("enter an IPv4 address: ")