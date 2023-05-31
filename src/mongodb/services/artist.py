from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__artistService__")

async def findOneArtistById(artistId: str):
    query = {}
    if artistId != None:
        query = {
            "_id": ObjectId(artistId)
        }
    artist = await database.artists.find_one(query)
    logger.warning(artist)
    return artist
