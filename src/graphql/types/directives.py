from strawberry.schema_directive import Location
from uuid import UUID

import strawberry

@strawberry.schema_directive(locations=[Location.OBJECT])
class Keys:
    fields: UUID