from ..db import database

import logging
logger = logging.getLogger("__artistService__")

def findOneArtist(query):
    artist = database.artists.find_one(query)
    return artist

# async def findOneArtistAndUpdate(query, update):
#     artist = await database.artists.find_one_and_update(query, update)

def insertOneArtist(artistDoc):
    artist = database.artists.insert_one(artistDoc)
    return artist

def updateOneArtist(query, update):
    database.artists.update_one(query, update)
    return True
