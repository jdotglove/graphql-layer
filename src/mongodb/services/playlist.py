from ..db import database

import logging
logger = logging.getLogger("__playlistService__")

async def findOnePlaylist(query):
    playlist = await database.playlists.find_one(query)
    return playlist

async def insertOnePlaylist(playlistDoc):
    playlist = await database.playlists.insert_one(playlistDoc)
    return playlist

async def updateOnePlaylist(query, update):
    await database.playlists.update_one(query, update)
    return True