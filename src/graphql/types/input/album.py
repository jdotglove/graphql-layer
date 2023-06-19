from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class AlbumPayload:
    albumType: Optional[str] = None
    artists: Optional[List[UUID]] = None
    availableMarkets: Optional[List[str]] = None
    name: Optional[str] = None
    releaseDate: Optional[str] = None
    releaseDatePercision: Optional[str] = None
    spotifyUri: Optional[str] = None
    totalTracks: Optional[int] = None

@strawberry.input
class AddOneAlbumPayloadInput:
    albumPayload: AlbumPayload

@strawberry.input
class GetOneAlbumQueryInput:
    albumId: str

@strawberry.input
class UpdateOneAlbumPayloadInput:
    albumId: str
    albumPayload: AlbumPayload