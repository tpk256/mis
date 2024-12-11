from pydantic import BaseModel

from .teacher import Teacher


class Subject(BaseModel):
    id: int
    title: str
    teachers: list[Teacher]
