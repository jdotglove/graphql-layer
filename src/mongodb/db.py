import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

import certifi
from src.config import AUDIONEST_MONGO_URI

ca = certifi.where()

# instantiate mongo client
client = AsyncIOMotorClient(AUDIONEST_MONGO_URI, tlsCAFile=ca)
database = client["mainStack"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)