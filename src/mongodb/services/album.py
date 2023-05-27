from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__albumService__")

async def findOneAlbumById(albumId: str):
    album = await database.albums.find_one({
        "_id": ObjectId(albumId)
    })
    logger.warning(album)
    return album
