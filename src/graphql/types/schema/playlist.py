from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from .track import Track

@strawberry.type
class Playlist:
    # Constructor to be used with db objects
    def __init__(self, playlist_dict):
        for key in playlist_dict:
            setattr(self, key, playlist_dict[key])

    # Public Class Fields
    name: str = strawberry.field(
        description="The name of the playlist."
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