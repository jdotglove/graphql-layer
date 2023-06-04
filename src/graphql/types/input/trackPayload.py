from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class TrackPayloadInput:
    album: Optional[List[UUID]] = None
    artists: Optional[List[UUID]] = None
    availableMarkets: Optional[List[str]] = None
    duration: Optional[int] = None
    explicit: Optional[bool] = None
    name: Optional[str] = None
    popularity: Optional[int] = None
    spotifyUri: Optional[str] = None
    trackNumber: Optional[int] = None