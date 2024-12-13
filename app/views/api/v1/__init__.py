from .questions import router as rt_que
from .teachers import router as rt_tea
from .subjects import router as rt_sub
from .topics import router as rt_top

from fastapi import APIRouter

router = APIRouter(prefix="/v1")
router.include_router(rt_que)
router.include_router(rt_tea)
router.include_router(rt_sub)
router.include_router(rt_top)
