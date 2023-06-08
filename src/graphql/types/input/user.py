from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class UserPayload:
    country: Optional[str] = None
    displayName: Optional[str] = None
    email: Optional[str] = None
    # images: TODO: come back to typing
    playlists: Optional[List[str]]
    spotifyUri: Optional[Optional[str]] = None
    topArtists: Optional[List[UUID]] = None
    topTracks: Optional[List[UUID]] = None

@strawberry.input
class AddOneUserPayloadInput:
    userPayload: UserPayload

@strawberry.input
class GetOneUserQueryInput:
    userId: str

@strawberry.input
class GetManyUsersQueryInput:
    userIds: List[str]

@strawberry.input
class UpdateOneUserPayloadInput:
    userId: str
    userPayload: UserPayload