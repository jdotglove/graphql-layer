from ..db import database

import logging
logger = logging.getLogger("__albumService__")

async def findOneAlbum(query):
    album = await database.albums.find_one(query)
    return album

async def insertOneAlbum(albumDoc):
    artist = await database.albums.insert_one(albumDoc)
    return artist

async def updateOneAlbum(query, update):
    await database.albums.update_one(query, update)
    return True
