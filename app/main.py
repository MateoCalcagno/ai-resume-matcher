from fastapi import FastAPI

from app.core.database import engine, Base
from app.models.user import User

from app.api.auth_routes import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "AI Resume Matcher API"
    }