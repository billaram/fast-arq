from fastapi import FastAPI
from fastapi import APIRouter
from app.api import api_router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router,
                      prefix="/api")



if __name__ == "__main__":
    uvicorn.run(app, log_level="debug", reload=True)