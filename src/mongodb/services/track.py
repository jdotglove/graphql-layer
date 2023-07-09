from ..db import database

import logging
logger = logging.getLogger("__trackService__")

def findOneTrack(query):
    return database.tracks.find_one(query)

def findManyTracks(query):
    return database.tracks.find(query)

def findOneTrackAndUpdate(query, update):
    return database.tracks.find_one_and_update(query, update)

def insertOneTrack(trackDoc):
    return database.tracks.insert_one(trackDoc)

def updateOneTrack(query, update):
    return database.tracks.update_one(query, update)