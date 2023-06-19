from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class ArtistPayload:
    albums: Optional[List[UUID]] = None
    name: Optional[str] = None
    genres: Optional[List[str]] = None
    popularity: Optional[int] = None
    spotifyUri: Optional[str] = None
    tracks: Optional[List[UUID]] = None

@strawberry.input
class AddOneArtistPayloadInput:
    artistPayload: ArtistPayload

@strawberry.input
class GetOneArtistQueryInput:
    artistId: str

@strawberry.input
class UpdateOneArtistPayloadInput:
    artistId: str
    artistPayload: ArtistPayload