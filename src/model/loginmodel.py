from pydantic import BaseModel
from pydantic import Field


class Login(BaseModel):
    user: str = Field(..., min_length=3)
    passwd: str = Field(..., min_length=3)
