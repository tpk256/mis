from fastapi import APIRouter

from dependency import db_session_depend
from models import Question
from db import get_questions_pydantic

router = APIRouter()


@router.get(
    path="/",
    response_model=list[Question]
)
async def get_questions(topic_id: int, db: db_session_depend):
    return get_questions_pydantic(db=db, topic_id=topic_id)

