from pydantic import BaseModel
from .subject import Subject


class Topic(BaseModel):
    id: int
    title: str

