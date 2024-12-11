from pydantic import BaseModel
from .topic import Topic


class Question(BaseModel):
    id: int
    text: str
    ans: str | None

