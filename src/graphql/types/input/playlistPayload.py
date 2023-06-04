from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class PlaylistPayloadInput:
    name: Optional[str]
    ownerId: Optional[UUID]
    ownerUri: Optional[str]
    spotifyUri: Optional[str]
    tracks: Optional[List[UUID]]