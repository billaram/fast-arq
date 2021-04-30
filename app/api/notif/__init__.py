from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def notif():
    return "I am notif router"

@router.post("/")
async def notif():
    return "I am notif router"