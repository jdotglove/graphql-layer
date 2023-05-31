from typing import Optional
from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from src.mongodb.services.album import findOneAlbumById
from src.mongodb.services.artist import findOneArtistById
from src.mongodb.services.playlist import findOnePlaylistById
from src.mongodb.services.track import findOneTrackById
from src.mongodb.services.user import findOneUserById


import logging
import strawberry

async def get_album(
    albumId: Optional[str],
) -> Album:
    print(f"Getting album - with id {albumId}")
    album = await findOneAlbumById(albumId)
    return Album(album)

async def get_artist(
    artistId: Optional[str],
) -> Artist:
    print(f"Getting artist - with id {artistId}")
    artist = await findOneArtistById(artistId)
    return Artist(artist)

async def get_playlist(
    playlistId: Optional[str],
) -> Playlist:
    print(f"Getting playlist - with id {playlistId}")
    playlist = await findOnePlaylistById(playlistId)
    return Playlist(playlist)

async def get_track(
    trackId: Optional[str],
) -> Track:
    print(f"Getting track - with id {trackId}")
    track = await findOneTrackById(trackId)
    return Track(track)

async def get_user(
    userId: Optional[str] = None,
) -> User:
    print(f"Getting user - with id {userId}")
    user = await findOneUserById(userId)
    return User(user)