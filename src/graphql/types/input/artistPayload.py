from typing import TYPE_CHECKING, Annotated, List

import strawberry

if TYPE_CHECKING:
    from src.graphql.types.schema.artist import Artist

@strawberry.input
class ArtistPayloadInput:
    name: str
    genres: List[str]
    popularity: int
    spotifyUri: str