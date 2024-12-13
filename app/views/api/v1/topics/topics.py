from fastapi import APIRouter

from models import Topic
from dependency import db_session_depend
from db import get_topics_pydantic

router = APIRouter()


@router.get(
    path="/",
    response_model=list[Topic]
)
async def get_topics(subject_id: int, db: db_session_depend):
    return get_topics_pydantic(db=db, subject_id=subject_id)