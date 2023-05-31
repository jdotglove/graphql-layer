from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

@strawberry.input
class ArtistPayloadInput:
    albums: List [UUID]
    name: str
    genres: List[str]
    popularity: int
    spotifyUri: str
    tracks: List[UUID]