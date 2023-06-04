from .base import BaseDBModel
# from ..directives import Keys
from typing import List
from uuid import UUID

import strawberry

@strawberry.type
class Track(BaseDBModel):
    # Constructor to be used with db objects
    def __init__(self, track_dict):
        for key in track_dict:
            setattr(self, key, track_dict[key])
    # Public Class Fields      
    album: UUID = strawberry.field(
        description="Id of the track album."
    )
    artists: List[UUID] = strawberry.field(
        description="The list of track artists ids."
    )
    availableMarkets: List[str] = strawberry.field(
        description="The list of available markets."
    )
    duration: int = strawberry.field(
        description="The duration of the track."
    )
    explicit: bool = strawberry.field(
        description="Whether or not the track is explicit."
    )
    name: str = strawberry.field(
        description="The name of the track."
    )
    popularity: int = strawberry.field(
        description="The popularity of the track."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the track."
    )
    trackNumber: int = strawberry.field(
        description="The number of the track on the the album."
    )