from .base import BaseDBModel
# from ..directives import Keys
from typing import List
from uuid import UUID

import strawberry

@strawberry.type
class Playlist(BaseDBModel):
    # Constructor to be used with db objects
    def __init__(self, playlist_dict):
        for key in playlist_dict:
            setattr(self, key, playlist_dict[key])
    # Public Class Fields
    _id: UUID = strawberry.field(
        description="The unique database id of the address."
    )
    name: str = strawberry.field(
        description="The name of the playlist."
    )
    ownerId: UUID = strawberry.field(
        description="The id for the owner of the playlist."
    )
    ownerUri: str = strawberry.field(
        description="The spotify uri for the owner of the playlist."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the playlist."
    )
    tracks: List[UUID] = strawberry.field(
        description="The list of playlist track ids ."
    )