from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from src.mongodb.services.album import findOneAlbumById
from .types.input.albumPayload import AlbumPayloadInput
from .types.input.artistPayload import ArtistPayloadInput
from .types.input.playlistPayload import PlaylistPayloadInput
from .types.input.trackPayload import TrackPayloadInput
from .types.input.userPayload import UserPayloadInput

from typing import Any, List

import logging
import strawberry

# @strawberry.input
# class AlbumPayloadInput:
#     albumType: str
#     # artists: List[Annotated["Artist", strawberry.lazy("src.graphql.types.schema.artist")]]
#     availableMarkets: List[str]
#     name: str
#     releaseDate: str
#     releaseDatePercision: str
#     spotifyUri: str
#     totalTracks: int

# ALBUM MUTATIONS
async def add_album(
    albumPayload: AlbumPayloadInput,
) -> Album:
    print(f"Adding album - with payload {albumPayload}")
    album = await insertOneAlbum(albumPayload)
    return Album(album)
async def update_album(
    albumId: str,
    albumPayload: AlbumPayloadInput #TODO: fix typing
) -> None:
    print(f"Updating album {albumId} - with payload {albumPayload}")
    await updateOneAlbum(albumId, albumPayload)
    return

# ARTIST MUTATIONS
async def add_artist(
    artistPayload: ArtistPayloadInput,
) -> Artist:
    print(f"Adding artist - with payload {artistPayload}")
    artist = await insertOneArtist(artistPayload)
    return Artist(artist)
async def update_artist(
    artistId: str,
    artistPayload: ArtistPayloadInput #TODO: fix typing
) -> None:
    print(f"Updating artist {artistId} - with payload {artistPayload}")
    await updateOneArtist({
        "_id": artistId
    }, artistPayload)
    return

# PLAYLIST MUTATIONS
async def add_playlist(
    playlistPayload: PlaylistPayloadInput,
) -> Playlist:
    print(f"Adding playlist - with payload {playlistPayload}")
    playlist = await insertOnePlaylist(playlistPayload)
    return Playlist(playlist)
async def update_playlist(
    playlistId: str,
    playlistPayload: PlaylistPayloadInput #TODO: fix typing
) -> None:
    print(f"Updating playlist {playlistId} - with payload {playlistPayload}")
    await updateOnePlaylist(playlistId, playlistPayload)
    return

# TRACK MUTATIONS
async def add_track(
    trackPayload: TrackPayloadInput #TODO: fix typing
) -> Track:
    print(f"Adding track - with payload {trackPayload}")
    track = await insertOneTrack(trackPayload)
    return Track(track)
async def update_track(
    trackId: str,
    trackPayload: TrackPayloadInput #TODO: fix typing
) -> None:
    print(f"Updating track {trackId} - with payload {trackPayload}")
    await updateOneTrack(trackId, trackPayload)
    return

# USER MUTATIONS
async def add_user(
    userPayload: UserPayloadInput #TODO: fix typing
) -> User:
    print(f"Adding user - with payload {userPayload}")
    user = await insertOneUser(userPayload)
    return User(user)
async def update_user(
    userId: str,
    userPayload: UserPayloadInput #TODO: fix typing
) -> None:
    print(f"Updating user {userId} - with payload {userPayload}")
    await updateOneUser(userPayload)
    return