from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class TrackPayload:
    albumType: Optional[str] = None
    artists: Optional[List[UUID]] = None
    availableMarkets: Optional[List[str]] = None
    name: Optional[str] = None
    releaseDate: Optional[str] = None
    releaseDatePercision: Optional[str] = None
    spotifyUri: Optional[str] = None
    totalTracks: Optional[int] = None

@strawberry.input
class AddOneTrackPayloadInput:
    trackPayload: TrackPayload

@strawberry.input
class GetOneTrackQueryInput:
    trackId: str

@strawberry.input
class UpdateOneTrackPayloadInput:
    trackId: str
    trackPayload: TrackPayload