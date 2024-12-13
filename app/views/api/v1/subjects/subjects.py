from fastapi import APIRouter

from models import Subject
from dependency import db_session_depend
from db import get_subjects_pydantic

router = APIRouter()


@router.get(
    path="/",
    response_model=list[Subject]
)
async def get_subjects(db: db_session_depend) -> list[Subject]:
    return get_subjects_pydantic(db=db)
