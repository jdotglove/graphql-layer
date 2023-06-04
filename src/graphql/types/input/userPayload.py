from typing import TYPE_CHECKING, Annotated, List, Optional
from uuid import UUID

import strawberry

@strawberry.input
class UserPayloadInput:
    country: Optional[str] = None
    displayName: Optional[str] = None
    email: Optional[str] = None
    # images: TODO: come back to typing
    playlists: Optional[List[str]]
    spotifyUri: Optional[Optional[str]] = None
    topArtists: Optional[List[UUID]] = None
    topTracks: Optional[List[UUID]] = None