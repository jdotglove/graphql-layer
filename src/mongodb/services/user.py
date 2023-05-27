from bson.objectid import ObjectId
from src.mongodb.db import database

import logging
logger = logging.getLogger("__userService__")

async def findOneUserById(userId: str):
    user = await database.users.find_one({
        "_id": ObjectId(userId)
    })
    logger.warning(user)
    return user
