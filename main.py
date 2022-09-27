from fastapi import FastAPI
from src.router import sponsor, event
from src.database import engine
from src import models

app = FastAPI()
app.include_router(event.router)
app.include_router(sponsor.router)

models.Base.metadata.create_all(engine)
