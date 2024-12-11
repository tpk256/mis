from fastapi import APIRouter
from models.subject import Subject


router = APIRouter()


@router.get(
    path="/",
    response_model=list[Subject]
)
async def get_subjects():
    return ...