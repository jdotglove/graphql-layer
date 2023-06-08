from .base import BaseDBModel
from typing import List
from uuid import UUID
from ..directives import Keys

import strawberry

@strawberry.type(directives=[Keys(fields="_id")])
class User(BaseDBModel):
    # Constructor to be used with db objects not sure why i need to keep this here
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