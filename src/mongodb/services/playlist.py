from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__playlistService__")

async def findOnePlaylistById(playlistId: str):
    playlist = await database.playlists.find_one({
        "_id": ObjectId(playlistId)
    })
    logger.warning(playlist)
    return playlist
