from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

@strawberry.input
class PlaylistPayloadInput:
    name: str
    ownerUri: str
    spotifyUri: str
    tracks: List[UUID]