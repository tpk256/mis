from fastapi import APIRouter

from .teachers import router as _router

router = APIRouter(prefix="/teachers")
router.include_router(_router)