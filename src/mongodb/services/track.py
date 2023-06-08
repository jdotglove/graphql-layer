from ..db import database

import logging
logger = logging.getLogger("__trackService__")

def findOneTrack(query):
    track = database.tracks.find_one(query)
    return track

def findManyTracks(query):
    tracks = database.tracks.find(query)
    return tracks

# async def findOneTrackAndUpdate(query, update):
#     track = await database.tracks.find_one_and_update(query, update)

def insertOneTrack(trackDoc):
    track = database.tracks.insert_one(trackDoc)
    return track

def updateOneTrack(query, update):
    database.tracks.update_one(query, update)
    return True