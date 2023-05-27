from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from src.graphql.types.schema.track import Track

@strawberry.input
class PlaylistPayloadInput:
    name: str
    ownerUri: str
    spotifyUri: str
    tracks: List[UUID]