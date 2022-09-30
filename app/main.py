from fastapi import FastAPI
from app.router import sponsor, event
from app.database import engine
from app import models

app = FastAPI()
app.include_router(event.router)
app.include_router(sponsor.router)

models.Base.metadata.create_all(engine)

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}