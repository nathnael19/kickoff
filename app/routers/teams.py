from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..models import teams as t
from ..schemas import teams
from ..db import database

router = APIRouter(prefix="/teams", tags=["Teams"])


# Create Score
@router.post("/", response_model=teams.TeamResponse)
def create_tournament(tournament: teams.TeamCreate, db: Session = Depends(database.get_db)):
    new_tournament = t.Team(**tournament.model_dump())
    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)
    return new_tournament

# Get All Score
@router.get("/", response_model=list[teams.TeamResponse])
def get_tournaments(db: Session = Depends(database.get_db)):
    return db.query(t.Team).all()

# Get Score by ID
@router.get("/{id}", response_model=teams.TeamResponse)
def get_tournament(id: int, db: Session = Depends(database.get_db)):
    tournament = db.query(t.Team).filter(t.Team.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    return tournament

# Update Score
@router.put("/{id}", response_model=teams.TeamResponse)
def update_tournament(id: int, updated: teams.TeamCreate, db: Session = Depends(database.get_db)):
    tournament = db.query(t.Team).filter(t.Team.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    for field, value in updated.dict().items():
        setattr(tournament, field, value)
    db.commit()
    db.refresh(tournament)
    return tournament

# Delete Score
@router.delete("/{id}")
def delete_tournament(id: int, db: Session = Depends(database.get_db)):
    tournament = db.query(t.Team).filter(t.Team.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    db.delete(tournament)
    db.commit()
    return {"message": "Scores deleted successfully"}
