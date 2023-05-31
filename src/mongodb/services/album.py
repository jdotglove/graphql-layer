from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__albumService__")

async def findOneAlbumById(albumId: str):
    query = {}
    if albumId != None:
        query = {
            "_id": ObjectId(albumId)
        }
    album = await database.albums.find_one(query)
    logger.warning(album)
    return album
