from fastapi import APIRouter
from models.question import Question


router = APIRouter()


@router.get(
    path="/",
    response_model=list[Question]
)
async def get_questions(topic_id: int):
    return ...