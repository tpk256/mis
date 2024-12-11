from fastapi import APIRouter

from .subjects import router as _router

router = APIRouter(prefix="/subjects")
router.include_router(_router)