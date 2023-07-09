from bson.objectid import ObjectId
from typing import Optional, List
from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from .types.input.album import GetOneAlbumQueryInput
from .types.input.artist import GetOneArtistQueryInput
from .types.input.playlist import GetOnePlaylistQueryInput
from .types.input.track import GetOneTrackQueryInput
from .types.input.user import GetOneUserQueryInput, GetManyUsersQueryInput
from src.mongodb.services.album import findOneAlbum
from src.mongodb.services.artist import findOneArtist
from src.mongodb.services.playlist import findOnePlaylist
from src.mongodb.services.track import findOneTrack, findManyTracks
from src.mongodb.services.user import findOneUser


import logging
import strawberry

logger = logging.getLogger("__queries__")

def get_one_album(
    query: GetOneAlbumQueryInput
):
    dbQuery = {}
    if query.albumId != None:
        dbQuery = {
            "_id": ObjectId(query.albumId)
        }
    print(f"Getting album - with {dbQuery}")
    album = findOneAlbum(dbQuery)
    return Album(album)

def get_many_albums(
    query: GetManyAlbumsQueryInput,
):
    dbQuery = {}
    if len(query.albumIds) != 0:
        dbQuery = {
            "_id": {
                "$in": query.albumIds
            }
        }

    print(f"Getting albums - with {dbQuery}")
    return findManyAlbums(dbQuery)

def get_one_artist(
    query: GetOneArtistQueryInput,
):
    dbQuery = {}
    if query.artistId != None:
        dbQuery = {
            "_id": ObjectId(query.artistId)
        }
    print(f"Getting artist - with {dbQuery}")
    artist = findOneArtist(dbQuery)
    return Artist(artist)

def get_many_artists(
    query: GetManyArtistsQueryInput,
):
    dbQuery = {}
    if len(query.artistIds) != 0:
        dbQuery = {
            "_id": {
                "$in": query.artistIds
            }
        }

    print(f"Getting artists - with {dbQuery}")
    return findManyArtists(dbQuery)

def get_one_playlist(
    query: GetOnePlaylistQueryInput,
):
    dbQuery = {}
    if query.playlistId != None:
        dbQuery = {
            "_id": ObjectId(query.playlistId)
        }
    print(f"Getting playlist - with {dbQuery}")
    playlist = findOnePlaylist(dbQuery)
    return Playlist(playlist)

def get_many_playlists(
    query: GetManyPlaylistsQueryInput,
):
    dbQuery = {}
    if len(query.playlistIds) != 0:
        dbQuery = {
            "_id": {
                "$in": query.playlistIds
            }
        }

    print(f"Getting playlists - with {dbQuery}")
    return findManyPlaylists(dbQuery)


def get_one_track(
    query: GetOneTrackQueryInput,
):
    dbQuery = {}
    if query.trackId != None:
        dbQuery = {
            "_id": ObjectId(query.trackId)
        }

    print(f"Getting track - with {dbQuery}")
    track = findOneTrack(dbQuery)
    return Track(track)

def get_many_tracks(
    query: GetManyTracksQueryInput,
):
    dbQuery = {}
    if len(query.trackIds) != 0:
        dbQuery = {
            "_id": {
                "$in": query.trackIds
            }
        }

    print(f"Getting tracks - with {dbQuery}")
    tracks = findManyTracks(dbQuery)
    return tracks

def get_one_user(
    query: GetOneUserQueryInput,
):
    dbQuery = {}
    if query.userId != None:
        dbQuery = {
            "_id": ObjectId(query.userId)
        }
    print(f"Getting user - with {dbQuery}")
    user = findOneUser(dbQuery)
    return User(user)

def get_many_users(
    query: GetManyUsersQueryInput,
):
    dbQuery = {}
    if len(query.userIds) != 0:
        dbQuery = {
            "_id": {
                "$in": query.userIds
            }
        }

    print(f"Getting users - with {dbQuery}")
    return findManyUsers(dbQuery)