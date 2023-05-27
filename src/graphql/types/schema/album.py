from typing import TYPE_CHECKING, Annotated, Any, List, TypeVar, Dict
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from .artist import Artist

@strawberry.type
class Album:
    # Constructor to be used with db objects
    def __init__(self, album_dict):
        for key in album_dict:
            setattr(self, key, album_dict[key])

    # Public Class Fields
    albumType: str = strawberry.field(
        description="The type of album."
    )
    artists: List[UUID] = strawberry.field(
        description="List of artist ids for reference."
    )
    availableMarkets: List[str] = strawberry.field(
        description="The list of available markets for the album."
    )
    name: str = strawberry.field(
        description="The name of the album."
    )
    releaseDate: str = strawberry.field(
        description="The release date of the album."
    )
    releaseDatePercision: str = strawberry.field(
        description="The name of the user."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the album."
    )
    totalTracks: int = strawberry.field(
        description="The name of the user."
    )