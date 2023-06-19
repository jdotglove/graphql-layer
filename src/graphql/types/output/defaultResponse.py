import strawberry

@strawberry.type
class DefaultResponseObject:
    # Constructor to be used with db objects
    def __init__(self, response_dict):
        for key in response_dict:
            setattr(self, key, response_dict[key])
    success: bool = strawberry.field(
        description="success indicator for the operation."
    )