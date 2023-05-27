from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from src.graphql.types.schema.user import User

@strawberry.input
class UserPayloadInput:
    country: str
    displayName: str
    email: str
    # images: TODO: come back to typing
    playlists: List[UUID]
    spotifyUri: str
    topArtists: List[UUID]
    topTracks: List[UUID]