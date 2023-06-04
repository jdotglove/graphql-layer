from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class ArtistPayloadInput:
    albums: Optional[List[UUID]] = None
    name: Optional[str] = None
    genres: Optional[List[str]] = None
    popularity: Optional[int] = None
    spotifyUri: Optional[str] = None
    tracks: Optional[List[UUID]] = None