# Module used compile all resolvers and declare Mutation and Query schemas
# Can also be extended to handle any subscriptions that may be needed
import typing
import strawberry

from .types.schema.album import Album
from .types.schema.artist import Artist
from .types.schema.playlist import Playlist
from .types.schema.track import Track
from .types.schema.user import User
from .types.output.defaultResponse import DefaultResponseObject

from .queries import get_album, get_artist, get_playlist, get_track, get_user
from .mutations import add_album, add_artist, add_playlist, add_track, add_user, update_album, update_artist, update_playlist, update_track, update_user

@strawberry.type
class Query:
    get_one_album: Album = strawberry.field(resolver=get_album)
    get_one_artist: Artist = strawberry.field(resolver=get_artist)
    get_one_playlist: Playlist = strawberry.field(resolver=get_playlist)
    get_one_track: Track = strawberry.field(resolver=get_track)
    get_one_user: User = strawberry.field(resolver=get_user)

@strawberry.type
class Mutation:
    add_one_album: Album = strawberry.mutation(resolver=add_album)
    add_one_artist: Artist = strawberry.mutation(resolver=add_artist)
    add_one_playlist: Playlist = strawberry.mutation(resolver=add_playlist)
    add_one_track: Track = strawberry.mutation(resolver=add_track)
    add_one_user: User = strawberry.mutation(resolver=add_user)
    update_one_album: DefaultResponseObject = strawberry.mutation(resolver=update_album)
    update_one_artis: DefaultResponseObject = strawberry.mutation(resolver=update_artist)
    update_one_playlist: DefaultResponseObject = strawberry.mutation(resolver=update_playlist)
    update_one_track: DefaultResponseObject = strawberry.mutation(resolver=update_track)
    update_one_user: DefaultResponseObject = strawberry.mutation(resolver=update_user)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=None)