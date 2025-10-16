from typing import Union
from app.db.database import Base, engine
from fastapi import FastAPI
from app.routers import router_tournaments,scores


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router_tournaments.router)
app.include_router(scores.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
