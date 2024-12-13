
from models import Teacher

from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from dependency import db_session_depend

from db import get_teachers_pydantic

router = APIRouter()


@router.get(
    path="/",
    response_model=list[Teacher]
)
async def get_teachers(subject_id: int, db: db_session_depend):
    return get_teachers_pydantic(db=db, subject_id=subject_id)