from fastapi import APIRouter
from app.api.notif import notif_router


api_router = APIRouter()

api_router.include_router(notif_router,
                      prefix="/notif")
