from fastapi import APIRouter

from .questions import router as _router

router = APIRouter(prefix="/questions")

router.include_router(_router)