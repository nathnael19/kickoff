from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..models import teams as t
from ..schemas import teams
from ..db import database

router = APIRouter(prefix="/teams", tags=["Teams"])


# Create Team
@router.post("/", response_model=teams.TeamResponse)
def create_team(team: teams.TeamCreate, db: Session = Depends(database.get_db)):
    new_team = t.Team(**team.model_dump())
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

# Get All Team
@router.get("/", response_model=list[teams.TeamResponse])
def get_teams(db: Session = Depends(database.get_db)):
    return db.query(t.Team).all()

# Get Team by ID
@router.get("/{id}", response_model=teams.TeamResponse)
def get_team(id: int, db: Session = Depends(database.get_db)):
    team = db.query(t.Team).filter(t.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    return team

# Update Team
@router.put("/{id}", response_model=teams.TeamResponse)
def update_team(id: int, updated: teams.TeamCreate, db: Session = Depends(database.get_db)):
    team = db.query(t.Team).filter(t.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    for field, value in updated.dict().items():
        setattr(team, field, value)
    db.commit()
    db.refresh(team)
    return team

# Delete Team
@router.delete("/{id}")
def delete_team(id: int, db: Session = Depends(database.get_db)):
    team = db.query(t.Team).filter(t.Team.id == id).first()
    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    db.delete(team)
    db.commit()
    return {"message": "Teams deleted successfully"}
