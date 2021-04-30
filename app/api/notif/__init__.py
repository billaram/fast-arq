from fastapi import APIRouter
from app.tasks.notif import send_notification

notif_router = APIRouter()


@notif_router.get("/")
async def notif():
    await send_notification("I am notifcation message")
    return "I am notif router"

@notif_router.post("/")
async def notif():
    return "I am notif router post"