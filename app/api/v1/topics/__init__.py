from fastapi import APIRouter

from .topics import router as _router

router = APIRouter(prefix="/topics")
router.include_router(_router)