from fastapi import FastAPI
from .routers import tournaments
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tournaments.router)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
