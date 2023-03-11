from pydantic import BaseModel
from pydantic import Field


class ChatGPTMessegeIn(BaseModel):
    message: str = Field(..., min_length=1, max_length=4096)


class ChatGPTMessageOut(BaseModel):
    id: str
    object: str
    created: str
    model: str
    usage: dict
    choices: list
