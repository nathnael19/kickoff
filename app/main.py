from fastapi import FastAPI
from app.db.database import Base, engine

# Import all models so tables are registered
from app.models import *  

# Import routers
from app.routers import router_tournaments, scores, teams, matches

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include your routers
app.include_router(router_tournaments.router)
app.include_router(scores.router)
app.include_router(teams.router)
app.include_router(matches.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}
