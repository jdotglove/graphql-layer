from ..db import database

import logging
logger = logging.getLogger("__albumService__")

def findOneAlbum(query):
    return database.albums.find_one(query)

def findOneAlbumAndUpdate(query, update):
    return database.albums.find_one_and_update(query, update)

def insertOneAlbum(albumDoc):
    return database.albums.insert_one(albumDoc)

def updateOneAlbum(query, update):
    return database.albums.update_one(query, update)
