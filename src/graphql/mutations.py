from bson.objectid import ObjectId
from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from src.mongodb.services.album import insertOneAlbum, updateOneAlbum
from src.mongodb.services.artist import insertOneArtist, updateOneArtist
from src.mongodb.services.playlist import insertOnePlaylist, updateOnePlaylist
from src.mongodb.services.track import insertOneTrack, updateOneTrack
from src.mongodb.services.user import insertOneUser, updateOneUser
from .types.input.albumPayload import AlbumPayloadInput
from .types.input.artistPayload import ArtistPayloadInput
from .types.input.playlistPayload import PlaylistPayloadInput
from .types.input.trackPayload import TrackPayloadInput
from .types.input.userPayload import UserPayloadInput
from .types.output.defaultResponse import DefaultResponseObject
from src.utils.dict import filterOutDictNoneValues

from typing import Any, List

import logging
import strawberry


# ALBUM MUTATIONS
async def add_album(
    albumPayload: AlbumPayloadInput,
) -> Album:
    print(f"Adding album - with payload {albumPayload}")
    album = await insertOneAlbum(albumPayload)
    return Album(album)

async def update_album(
    albumId: str,
    albumPayload: AlbumPayloadInput
) -> DefaultResponseObject:
    formattedAlbumPayload = filterOutDictNoneValues(strawberry.asdict(albumPayload))
    print(f"Updating album {albumId} - with payload {formattedAlbumPayload}")
    await updateOneAlbum({
        "_id": ObjectId(albumId)
    }, {
        "$set": formattedAlbumPayload
    })
    return DefaultResponseObject({
        "success": True
    })

# ARTIST MUTATIONS
async def add_artist(
    artistPayload: ArtistPayloadInput,
) -> Artist:
    print(f"Adding artist - with payload {artistPayload}")
    artist = await insertOneArtist(artistPayload)
    return Artist(artist)

async def update_artist(
    artistId: str,
    artistPayload: ArtistPayloadInput
) -> DefaultResponseObject:
    formattedArtistPayload = filterOutDictNoneValues(strawberry.asdict(artistPayload))
    print(f"Updating artist {artistId} - with formatted payload {formattedArtistPayload}")
    await updateOneArtist({
        "_id": ObjectId(artistId)
    }, {
        "$set": formattedArtistPayload
    })
    return DefaultResponseObject({
        "success": True
    })

# PLAYLIST MUTATIONS
async def add_playlist(
    playlistPayload: PlaylistPayloadInput,
) -> Playlist:
    print(f"Adding playlist - with payload {playlistPayload}")
    playlist = await insertOnePlaylist(playlistPayload)
    return Playlist(playlist)

async def update_playlist(
    playlistId: str,
    playlistPayload: PlaylistPayloadInput
) -> DefaultResponseObject:
    formattedPlaylistPayload = filterOutDictNoneValues(strawberry.asdict(playlistPayload))
    print(f"Updating playlist {playlistId} - with formatted payload {formattedPlaylistPayload}")
    await updateOnePlaylist({
        "_id": ObjectId(playlistId)
    }, {
        "$set": formattedPlaylistPayload
    })
    return DefaultResponseObject({
        "success": True
    })

# TRACK MUTATIONS
async def add_track(
    trackPayload: TrackPayloadInput
) -> Track:
    print(f"Adding track - with payload {trackPayload}")
    track = await insertOneTrack(trackPayload)
    return Track(track)

async def update_track(
    trackId: str,
    trackPayload: TrackPayloadInput
) -> DefaultResponseObject:
    formattedTrackPayload = filterOutDictNoneValues(strawberry.asdict(trackPayload))
    print(f"Updating track {trackId} - with formatted payload {formattedTrackPayload}")
    await updateOneTrackById({
        "_id": ObjectId(trackId)
    }, {
        "$set": formattedTrackPayload
    })
    return DefaultResponseObject({
        "success": True
    })

# USER MUTATIONS
async def add_user(
    userPayload: UserPayloadInput
) -> User:
    print(f"Adding user - with payload {userPayload}")
    user = await insertOneUser(userPayload)
    return User(user)

async def update_user(
    userId: str,
    userPayload: UserPayloadInput
) -> DefaultResponseObject:
    formattedUserPayload = filterOutDictNoneValues(strawberry.asdict(userPayload))
    print(f"Updating user {userId} - with formatted payload {formattedUserPayload}")
    await updateOneUser({
        "_id": ObjectId(userId)
    }, {
        "$set": formattedUserPayload
    })
    return DefaultResponseObject({
        "success": True
    })