from .base import BaseDBModel
from ..directives import Keys
from typing import List, Type
from uuid import UUID
from ..directives import Keys

import strawberry

@strawberry.type
class TrackAudioFeatures:
    # Constructor to be used with db objects
    def __init__(self, audio_features_dict):
        for key in audio_features_dict:
            setattr(self, key, audio_features_dict[key])

    acousticness: float = strawberry.field(
        description="Acousticness feature of track."
    )
    analysisUrl: str = strawberry.field(
        description="Analysis url of track."
    )
    danceability: float = strawberry.field(
        description="Danceability feature of track."
    )
    energy: float = strawberry.field(
        description="Energy feature of track."
    )
    instrumentalness: float = strawberry.field(
        description="Instrumentalness feature of track."
    )
    key: int = strawberry.field(
        description="Key of track."
    )
    liveness: float = strawberry.field(
        description="Liveness feature of track."
    )
    loudness: float = strawberry.field(
        description="Loudness feature of track."
    )
    mode: int = strawberry.field(
        description="Mode feature of track."
    )
    speechiness: float = strawberry.field(
        description="Speechiness feature of track."
    )
    spotifyUri: str = strawberry.field(
        description="Spotfy uri track."
    )
    tempo: float = strawberry.field(
        description="Tempo feature of track."
    )
    timeSignature: int = strawberry.field(
        description="time signature of track."
    )
    valence: float = strawberry.field(
        description="Valence feature of track."
    )

@strawberry.type(directives=[Keys(fields="_id")])
class Track(BaseDBModel):
    # Constructor to be used with db objects
    def __init__(self, track_dict):
        for key in track_dict:
            if key == 'audioFeatures':
                setattr(self, key, TrackAudioFeatures(track_dict[key]))    
            else:
                setattr(self, key, track_dict[key])

    # Public Class Fields      
    album: UUID = strawberry.field(
        description="Id of the track album."
    )
    artists: List[UUID] = strawberry.field(
        description="The list of track artists ids and names."
    )
    audioFeatures: TrackAudioFeatures = strawberry.field(
        description="THe audio features of the track."
    )
    availableMarkets: List[str] = strawberry.field(
        description="The list of available markets."
    )
    durationMs: int = strawberry.field(
        description="The duration (in milliseconds) of the track."
    )
    explicit: bool = strawberry.field(
        description="Whether or not the track is explicit."
    )
    name: str = strawberry.field(
        description="The name of the track."
    )
    popularity: int = strawberry.field(
        description="The popularity of the track."
    )
    spotifyUri: str = strawberry.field(
        description="The spotify uri of the track."
    )
    trackNumber: int = strawberry.field(
        description="The number of the track on the the album."
    )