#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 01 30
#Course:        CSC425 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the method definitions to save an object 
#   from the game state to the local device and
#   load an object from the local device to the game state.
#   
#   It uses picling via the pickle library to implement this.

import pickle

#save object
def save_object(f_token):
    folder = "./savefiles/"
    filename = str(str(folder) + str(f_token.object_id) + ".gamesave")

    file = open(filename, "wb")

    pickle.dump(f_token, file)
#

#load object
def load_object(f_filename):
    file = open(f_filename, 'rb')
    object = pickle.load(file)
    return object
#