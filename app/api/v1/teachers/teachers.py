from fastapi import APIRouter
from models.teacher import Teacher



router = APIRouter()


@router.get(
    path="/",
    response_model=list[Teacher]
)
async def get_teachers(subject_id: id):
    return ...