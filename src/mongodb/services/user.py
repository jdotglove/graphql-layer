from ..db import database

import logging
logger = logging.getLogger("__userService__")

async def findOneUser(query):
    user = await database.users.find_one(query)
    return user

async def insertOneUser(userDoc):
    user = await database.users.insert_one(userDoc)
    return user

async def updateOneUser(query, update):
    await database.users.update_one(query, update)
    return True