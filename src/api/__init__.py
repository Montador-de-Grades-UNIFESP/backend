from .auth import router as auth_router
from .common import router as common_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(auth_router.router, prefix="/auth")
router.include_router(common_router.router, prefix="/common")
