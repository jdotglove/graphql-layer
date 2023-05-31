from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__trackService__")

async def findOneTrackById(trackId: str):
    query = {}
    if trackId != None:
        query = {
            "_id": ObjectId(trackId)
        }
    track = await database.tracks.find_one(query)
    logger.warning(track)
    return track
