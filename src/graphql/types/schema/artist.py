from uuid import UUID
from .base import BaseDBModel
from ..directives import Keys
from typing import List

import strawberry

@strawberry.type(directives=[Keys(fields="_id")])
class Artist(BaseDBModel):
    # Constructor to be used with db objects
    def __init__(self, artist_dict):
        for key in artist_dict:
            setattr(self, key, artist_dict[key])
    # Public Class Fields
    albums: List[UUID] = strawberry.field(
        description="The list of albums for an artist."
    )
    name: str = strawberry.field(
        description="The name of the artist."
    )
    genres: List[str] = strawberry.field(
        description="The list genres of the artist."
    )
    popularity: int = strawberry.field(
        description="The popularity of the artist."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the artist."
    )
    tracks: List[UUID] = strawberry.field(
        description="The list of tracks for an artist."
    )