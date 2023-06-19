from ..db import database

import logging
logger = logging.getLogger("__userService__")

def findOneUser(query):
    user = database.users.find_one(query)
    return user

def findOneUserAndUpdate(query, update):
    database.users.find_one_and_update(query, update)
    return True

def insertOneUser(userDoc):
    user = database.users.insert_one(userDoc)
    return user

def updateOneUser(query, update):
    database.users.update_one(query, update)
    return