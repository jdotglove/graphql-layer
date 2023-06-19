# Module used compile all resolvers and declare Mutation and Query schemas
# Can also be extended to handle any subscriptions that may be needed
from strawberry.schema.config import StrawberryConfig
from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from .types.output.defaultResponse import DefaultResponseObject
from .queries import get_one_album, get_one_artist, get_one_playlist, get_one_track, get_one_user, get_many_tracks
from .mutations import add_one_album, add_one_artist, add_one_playlist, add_one_track, add_one_user, update_one_album, update_one_artist, update_one_playlist, update_one_track, update_one_user
from typing import List

import strawberry

@strawberry.type
class Query:
    getOneAlbum: Album = strawberry.field(resolver=get_one_album)
    getOneArtist: Artist = strawberry.field(resolver=get_one_artist)
    getOnePlaylist: Playlist = strawberry.field(resolver=get_one_playlist)
    getOneTrack: Track = strawberry.field(resolver=get_one_track)
    getOneUser: User = strawberry.field(resolver=get_one_user)
    # get_many_albums: List[Album] = strawberry.field(resolver=get_albums)
    # get_many_artists: List[Artist] = strawberry.field(resolver=get_artists)
    # get_many_playlists: List[Playlist] = strawberry.field(resolver=get_playlists)
    getManyTracks: List[Track] = strawberry.field(resolver=get_many_tracks)
    # get_many_users: List[User] = strawberry.field(resolver=get_users)

@strawberry.type
class Mutation:
    addOneAlbum: Album = strawberry.mutation(resolver=add_one_album)
    addOneArtist: Artist = strawberry.mutation(resolver=add_one_artist)
    addOnePlaylist: Playlist = strawberry.mutation(resolver=add_one_playlist)
    addOneTrack: Track = strawberry.mutation(resolver=add_one_track)
    addOneUser: User = strawberry.mutation(resolver=add_one_user)
    updateOneAlbum: DefaultResponseObject = strawberry.mutation(resolver=update_one_album)
    updateOneArtist: DefaultResponseObject = strawberry.mutation(resolver=update_one_artist)
    updateOnePlaylist: DefaultResponseObject = strawberry.mutation(resolver=update_one_playlist)
    updateOneTrack: DefaultResponseObject = strawberry.mutation(resolver=update_one_track)
    updateOneUser: DefaultResponseObject = strawberry.mutation(resolver=update_one_user)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=None, config=StrawberryConfig(auto_camel_case=False))