from typing import List

from pydantic import Field

from app.schemas.base import APIBaseCreateSchema, APIBaseSchema, PyObjectId


class ChannelSchema(APIBaseSchema):
    kind: str
    owner: PyObjectId = Field()


class DMChannelSchema(ChannelSchema):
    members: List[PyObjectId] = []

    class Config:
        schema_extra = {
            "example": {
                "id": "61e17018c3ee162141baf5c9",
                "kind": "dm",
                "members": ["61e17018c3ee162141baf5c1", "61e17018c3ee162141baf5c2", "61e17018c3ee162141baf5c3"],
                "owner": "61e17018c3ee162141baf5c1",
            }
        }


class ServerChannelSchema(ChannelSchema):
    server: PyObjectId = Field()
    name: str = Field()

    class Config:
        schema_extra = {
            "example": {
                "id": "61e17018c3ee162141baf5c9",
                "kind": "server",
                "name": "🔥-shilling",
                "server": "61e17018c3ee162141baf5c1",
                "owner": "61e17018c3ee162141baf5c1",
            }
        }


class ChannelCreateSchema(APIBaseCreateSchema):
    kind: str


class DMChannelCreateSchema(ChannelCreateSchema):
    members: List[str]


class ServerChannelCreateSchema(ChannelCreateSchema):
    server: str
    name: str
