# Module used compile all resolvers and declare Mutation and Query schemas
# Can also be extended to handle any subscriptions that may be needed
import typing
import strawberry

from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User

from .queries import get_album, get_artist, get_playlist, get_track, get_user
from .mutations import add_album, add_artist, add_playlist, add_track, add_user
from .mutations import update_album, update_artist, update_playlist, update_track, update_user

@strawberry.type
class Query:
    getOneAlbum: Album = strawberry.field(resolver=get_album)
    getOneArtist: Artist = strawberry.field(resolver=get_artist)
    getOnePlaylist: Playlist = strawberry.field(resolver=get_playlist)
    getOneTrack: Track = strawberry.field(resolver=get_track)
    getOneUser: User = strawberry.field(resolver=get_user)

@strawberry.type
class Mutation:
    addOneAlbum: Album = strawberry.mutation(resolver=add_album)
    addOneArtist: Artist = strawberry.mutation(resolver=add_artist)
    addOnePlaylist: Playlist = strawberry.mutation(resolver=add_playlist)
    addOneTrack: Track = strawberry.mutation(resolver=add_track)
    addOneUser: User = strawberry.mutation(resolver=add_user)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=None)