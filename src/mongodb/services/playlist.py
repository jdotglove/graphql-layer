from ..db import database

import logging
logger = logging.getLogger("__playlistService__")

def findOnePlaylist(query):
    playlist = database.playlists.find_one(query)
    return playlist

# async def findOnePlaylistAndUpdate(query, update):
#     playlist = await database.playlists.find_one_and_update(query, update)

def insertOnePlaylist(playlistDoc):
    playlist = database.playlists.insert_one(playlistDoc)
    return playlist

def updateOnePlaylist(query, update):
    database.playlists.update_one(query, update)
    return True