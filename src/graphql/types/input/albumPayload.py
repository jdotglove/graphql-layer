from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

@strawberry.input
class AlbumPayloadInput:
    albumType: str
    artists: List[UUID]
    availableMarkets: List[str]
    name: str
    releaseDate: str
    releaseDatePercision: str
    spotifyUri: str
    totalTracks: int