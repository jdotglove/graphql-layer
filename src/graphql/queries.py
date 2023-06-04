from bson.objectid import ObjectId
from typing import Optional
from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from src.mongodb.services.album import findOneAlbum
from src.mongodb.services.artist import findOneArtist
from src.mongodb.services.playlist import findOnePlaylist
from src.mongodb.services.track import findOneTrack
from src.mongodb.services.user import findOneUser


import logging
import strawberry

logger = logging.getLogger("__queries__")

async def get_album(
    albumId: Optional[str],
) -> Album:
    query = {}
    if albumId != None:
        query = {
            "_id": ObjectId(albumId)
        }
    print(f"Getting album - with {query}")
    album = await findOneAlbum(query)
    return Album(album)

async def get_artist(
    artistId: Optional[str],
) -> Artist:
    query = {}
    if artistId != None:
        query = {
            "_id": ObjectId(artistId)
        }
    print(f"Getting artist - with {query}")
    artist = await findOneArtist(query)
    return Artist(artist)

async def get_playlist(
    playlistId: Optional[str],
) -> Playlist:
    query = {}
    if playlistId != None:
        query = {
            "_id": ObjectId(playlistId)
        }
    print(f"Getting playlist - with {query}")
    playlist = await findOnePlaylist(query)
    return Playlist(playlist)

async def get_track(
    trackId: Optional[str],
) -> Track:
    query = {}
    if trackId != None:
        query = {
            "_id": ObjectId(trackId)
        }

    print(f"Getting track - with {query}")
    track = await findOneTrack(query)
    return Track(track)

async def get_user(
    userId: Optional[str] = None,
) -> User:
    query = {}
    if userId != None:
        query = {
            "_id": ObjectId(userId)
        }
    print(f"Getting user - with {query}")
    user = await findOneUser(query)
    print(f"User: {user}")
    return User(user)