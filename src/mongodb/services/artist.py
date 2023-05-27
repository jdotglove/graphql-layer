from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__artistService__")

async def findOneArtistById(artistId: str):
    artist = await database.artists.find_one({
        "_id": ObjectId(artistId)
    })
    logger.warning(artist)
    return artist
