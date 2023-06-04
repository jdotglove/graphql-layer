from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class AlbumPayloadInput:
    albumType: Optional[str] = None
    artists: Optional[List[UUID]] = None
    availableMarkets: Optional[List[str]]
    name: Optional[str]
    releaseDate: Optional[str]
    releaseDatePercision: Optional[str]
    spotifyUri: Optional[str]
    totalTracks: Optional[int]