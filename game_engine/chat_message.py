#Author:        Dylan E. Wheeler
#Email:         dylan.wheeler@usm.edu
#Date:          2019 02 12
#Course:        CSC242 - Software Engineering II
#Prof.:         Dr. A. Louise Perkins

#This file contains the class definition for a chat message,
#   to be sent between players by players and appear in the 
#   chat log in the main GUI.
#
#   A "message" includes not just the string of the message but also:
#       the speech type (spoken word, action description, etc) 
#       the UUIDs (.object_id) of the speaker and of all receipiants 
#           for whom the message is visible
#       the visibility type (public, whisper, etc)
#       the language in which the message was spoken
#       and linked game objects in the message

import uuid

class ChatMessage:

    def __init__(self, f_speaker, f_type, f_visibility, f_message = "", f_language = "", f_objects = None): 
        self.object_id = uuid.uuid1()

        self.speaker_id = f_speaker.object_id
        self.speaker_name = f_speaker.name

        self.type = f_type
        self.visibility = f_visibility

        self.message = f_mesage
        self.language = f_language

        self.trunk = {}
        if f_objects != None:
            for each_object in f_objects:
                self.trunk[each_object.object_id] = each_object
    #end initializer



#end clas chat message