from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class PlaylistPayload:
    name: Optional[str] = None
    ownerId: Optional[UUID] = None
    ownerUri: Optional[str] = None
    spotifyUri: Optional[str] = None
    tracks: Optional[List[UUID]] = None

@strawberry.input
class AddOnePlaylistPayloadInput:
    playlistPayload: PlaylistPayload

@strawberry.input
class GetOnePlaylistQueryInput:
    playlistId: str

@strawberry.input
class UpdateOnePlaylistPayloadInput:
    playlistId: str
    playlistPayload: PlaylistPayload