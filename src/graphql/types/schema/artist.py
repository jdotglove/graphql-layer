from typing import List

import strawberry

@strawberry.type
class Artist:
    # Constructor to be used with db objects
    def __init__(self, artist_dict):
        for key in artist_dict:
            setattr(self, key, artist_dict[key])

    # Public Class Fields
    name: str = strawberry.field(
        description="The name of the artist."
    )
    genres: List[str] = strawberry.field(
        description="The list genres of the artist."
    )
    popularity: int = strawberry.field(
        description="The popularity of the artist."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the artist."
    )