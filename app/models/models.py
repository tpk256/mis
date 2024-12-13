from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Teacher(Base):
    name: str


class Subject(Base):
    title: str


class Question(Base):
    text: str
    ans: str | None
    topic_id: int


class Topic(Base):
    title: str
    subject_id: int










