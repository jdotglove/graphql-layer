from ..db import database

import logging
logger = logging.getLogger("__artistService__")

async def findOneArtist(query):
    artist = await database.artists.find_one(query)
    return artist

async def insertOneArtist(artistDoc):
    artist = await database.artists.insert_one(artistDoc)
    return artist

async def updateOneArtist(query, update):
    await database.artists.update_one(query, update)
    return True
