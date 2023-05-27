from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__trackService__")

async def findOneTrackById(trackId: str):
    track = await database.tracks.find_one({
        "_id": ObjectId(trackId)
    })
    logger.warning(track)
    return track
