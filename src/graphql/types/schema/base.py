from ..directives import Keys
from datetime import datetime
from uuid import UUID

import strawberry

@strawberry.interface(directives=[Keys(fields="_id")])
class BaseDBModel:
    _id: UUID = strawberry.field(
        description="The unique database id of the address."
    )