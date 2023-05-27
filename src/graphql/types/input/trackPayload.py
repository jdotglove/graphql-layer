from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from src.graphql.types.schema.track import Track

@strawberry.input
class TrackPayloadAlbumInput:
    albumType: str
    artists: List[UUID]
    availableMarkets: List[str]
    name: str
    releaseDate: str
    releaseDatePercision: str
    spotifyUri: str
    totalTracks: int

@strawberry.input
class TrackPayloadInput:
    album: TrackPayloadAlbumInput
    artists: List[UUID]
    availableMarkets: List[str]
    duration: int
    explicit: bool
    name: str
    popularity: int
    spotifyUri: str
    trackNumber: int