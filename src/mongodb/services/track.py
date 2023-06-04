from ..db import database

import logging
logger = logging.getLogger("__trackService__")

async def findOneTrack(query):
    track = await database.tracks.find_one(query)
    return track

async def insertOneTrack(trackDoc):
    track = await database.tracks.insert_one(trackDoc)
    return track

async def updateOneTrack(query, update):
    await database.tracks.update_one(query, update)
    return True