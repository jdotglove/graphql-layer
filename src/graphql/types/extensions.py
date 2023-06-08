from strawberry.types import Info
from typing import Any
from strawberry.extensions import FieldExtension, SchemaExtension

class MutationInputExtension(FieldExtension):
    def resolve(self, _next, root: Any, info: Info, *args, **kwargs):
        input = {}
        for a in kwargs:
            setattr(a, input[a])
        return _next(root, info, *args, input)