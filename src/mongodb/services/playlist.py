from ..db import database

import logging
logger = logging.getLogger("__playlistService__")

def findOnePlaylist(query):
    return database.playlists.find_one(query)

def findOnePlaylistAndUpdate(query, update):
    return database.playlists.find_one_and_update(query, update)

def insertOnePlaylist(playlistDoc):
    return database.playlists.insert_one(playlistDoc)

def updateOnePlaylist(query, update):
    return database.playlists.update_one(query, update)