from ..db import database

import logging
logger = logging.getLogger("__albumService__")

def findOneAlbum(query):
    album = database.albums.find_one(query)
    return album

# async def findOneAlbumAndUpdate(query, update):
#     album = await database.albums.find_one_and_update(query, update)
#     return album

def insertOneAlbum(albumDoc):
    album = database.albums.insert_one(albumDoc)
    return album

def updateOneAlbum(query, update):
    database.albums.update_one(query, update)
    return True
