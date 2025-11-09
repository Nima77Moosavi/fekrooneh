from fastapi import FastAPI, APIRouter
from app.users.routers import router as users_router


app = FastAPI()

router = APIRouter()


app.include_router(users_router)


@app.get("/")
async def health():
    return {"status": "ok"}
