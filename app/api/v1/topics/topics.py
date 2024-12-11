from fastapi import APIRouter
from models.topic import Topic


router = APIRouter()


@router.get(
    path="/",
    response_model=list[Topic]
)
async def get_teachers(subject_id: id):
    return ...