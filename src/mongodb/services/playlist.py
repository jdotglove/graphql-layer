from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__playlistService__")

async def findOnePlaylistById(playlistId: str):
    query = {}
    if playlistId != None:
        query = {
            "_id": ObjectId(playlistId)
        }
    playlist = await database.playlists.find_one(query)
    logger.warning(playlist)
    return playlist
