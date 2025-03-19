import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.user.router import router as user_router
from src.settings import settings


app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)

ALLOW_ORIGINS = [settings.FRONTEND_BASE_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app="src.main:app", host=settings.API_HOST, port=settings.API_PORT)
