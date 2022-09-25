from fastapi import FastAPI
# from src.router import event, sponsor

app = FastAPI()
# app.include_router(event.router)
# app.include_router(sponsor.router)

@app.get("/")
def read_root():
    return {"Hello": "World by Bir"}