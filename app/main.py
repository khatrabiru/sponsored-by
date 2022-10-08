from fastapi import FastAPI
from app.router import sponsor, event
from app.database import engine
from app import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(event.router)
app.include_router(sponsor.router)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}