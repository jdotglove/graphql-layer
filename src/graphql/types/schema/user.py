from typing import TYPE_CHECKING, Annotated, List
from uuid import UUID

import strawberry

if TYPE_CHECKING:
    from .artist import Artist
    from .playlist import Playlist
    from .track import Track

@strawberry.type
class User:
    # Constructor to be used with db objects
    def __init__(self, user_dict):
        for key in user_dict:
            setattr(self, key, user_dict[key])

    # Public Class Fields
    country: str = strawberry.field(
        description="The country of the user."
    )
    displayName: str = strawberry.field(
        description="The display name of the user."
    )
    email: str = strawberry.field(
        description="The email of the user."
    )
    # images: TODO: come back to typing
    playlists: List[UUID] = strawberry.field(
        description="The list of ids for the user's playlists."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the user."
    )
    topArtists: List[UUID] = strawberry.field(
        description="The list of ids of the top artists for user."
    )
    topTracks: List[UUID] = strawberry.field(
        description="The list of of ids of the top tracks for user."
    )