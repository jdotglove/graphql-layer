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
from .types.input.album import AddOneAlbumPayloadInput, UpdateOneAlbumPayloadInput
from .types.input.artist import AddOneArtistPayloadInput, UpdateOneArtistPayloadInput
from .types.input.playlist import AddOnePlaylistPayloadInput, UpdateOnePlaylistPayloadInput
from .types.input.track import AddOneTrackPayloadInput, UpdateOneTrackPayloadInput
from .types.input.user import AddOneUserPayloadInput, UpdateOneUserPayloadInput
from .types.output.defaultResponse import DefaultResponseObject
from src.utils.dict import filterOutDictNoneValues

from typing import Annotated, Any, List

import logging
import strawberry

# ALBUM MUTATIONS
def add_one_album(
    input: AddOneAlbumPayloadInput = strawberry.argument(
        description="Input to be used to create a new album document."
    )
):
    print(f"Adding album - with payload {albumPayload}")
    album = insertOneAlbum(albumPayload)
    return Album(album)

def update_one_album(
    input: UpdateOneAlbumPayloadInput = strawberry.argument(
        description="Input to be used to locate and update an an album document."
    )
):
    formattedAlbumPayload = filterOutDictNoneValues(strawberry.asdict(input.albumPayload))
    print(f"Updating album {input.albumId} - with payload {formattedAlbumPayload}")
    updateOneAlbum({
        "_id": ObjectId(albumId),
    }, {
        "$set": formattedAlbumPayload,
    })
    return DefaultResponseObject({
        "success": True,
    })

# ARTIST MUTATIONS
def add_one_artist(
    input: AddOneArtistPayloadInput = strawberry.argument(
        description="Input to be used to create a new artist document."
    )
):
    print(f"Adding artist - with payload {input.artistPayload}")
    artist = insertOneArtist(input.artistPayload)
    return Artist(artist)

def update_one_artist(
    input: UpdateOneArtistPayloadInput = strawberry.argument(
        description="Input to be used to locate and update an artist document."
    )
):
    formattedArtistPayload = filterOutDictNoneValues(strawberry.asdict(input.artistPayload))
    print(f"Updating artist {input.artistId} - with formatted payload {formattedArtistPayload}")
    updateOneArtist({
        "_id": ObjectId(input.artistId),
    }, {
        "$set": input.formattedArtistPayload,
    })
    return DefaultResponseObject({
        "success": True,
    })

# PLAYLIST MUTATIONS
def add_one_playlist(
    input: AddOnePlaylistPayloadInput = strawberry.argument(
        description="Input to be used to create a new playlist document."
    )
):
    print(f"Adding playlist - with payload {input.playlistPayload}")
    playlist = insertOnePlaylist(input.playlistPayload)
    return Playlist(playlist)

def update_one_playlist(
    input: UpdateOnePlaylistPayloadInput = strawberry.argument(
        description="Input to be used to locate and update a playlist document."
    )
):
    formattedPlaylistPayload = filterOutDictNoneValues(strawberry.asdict(input.playlistPayload))
    print(f"Updating playlist {input.playlistId} - with formatted payload {formattedPlaylistPayload}")
    updateOnePlaylist({
        "_id": ObjectId(input.playlistId),
    }, {
        "$set": formattedPlaylistPayload,
    })
    return DefaultResponseObject({
        "success": True,
    })

# TRACK MUTATIONS
def add_one_track(
    input: AddOneTrackPayloadInput = strawberry.argument(
        description="Input to be used to create a new track document."
    )
):
    print(f"Adding track - with payload {input.trackPayload}")
    track = insertOneTrack(input.trackPayload)
    return Track(track)

def update_one_track(
    input: UpdateOneTrackPayloadInput = strawberry.argument(
        description="Input to be used to locate and update a track document."
    )
):
    formattedTrackPayload = filterOutDictNoneValues(strawberry.asdict(input.trackPayload))
    print(f"Updating track {input.trackId} - with formatted payload {formattedTrackPayload}")
    updateOneTrackById({
        "_id": ObjectId(input.trackId),
    }, {
        "$set": formattedTrackPayload,
    })
    return DefaultResponseObject({
        "success": True,
    })

# USER MUTATIONS
def add_one_user(
    input: AddOneUserPayloadInput = strawberry.argument(
        description="Input to be used to create a new user document."
    )
):
    print(f"Adding user - with payload {input.userPayload}")
    user = insertOneUser(input.userPayload)
    return User(user)

def update_one_user(
    input: UpdateOneUserPayloadInput = strawberry.argument(
        description="Input to be used to locate and update a user document."
    )
):
    formattedUserPayload = filterOutDictNoneValues(strawberry.asdict(input. userPayload))
    print(f"Updating user {input.userId} - with formatted payload {formattedUserPayload}")
    updateOneUser({
        "_id": ObjectId(input.userId),
    }, {
        "$set": formattedUserPayload,
    })
    return DefaultResponseObject({
        "success": True,
    })