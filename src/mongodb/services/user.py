from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__userService__")

async def findOneUserById(userId: str):
    query = {}
    if userId != None:
        query = {
            "_id": ObjectId(userId)
        }
    user = await database.users.find_one(query)
    logger.warning(user)
    return user
