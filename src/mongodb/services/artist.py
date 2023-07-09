from ..db import database

import logging
logger = logging.getLogger("__artistService__")

def findOneArtist(query):
    return database.artists.find_one(query)

def findOneArtistAndUpdate(query, update):
    return database.artists.find_one_and_update(query, update)

def insertOneArtist(artistDoc):
    return database.artists.insert_one(artistDoc)

def updateOneArtist(query, update):
    return database.artists.update_one(query, update)
