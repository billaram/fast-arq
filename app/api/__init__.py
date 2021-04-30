from fastapi import APIRouter

router = APIRouter()
router.include_router(user_router,
                      prefix="/notif")