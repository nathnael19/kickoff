from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..models import scores as s
from ..schemas import scores
from ..db import database

router = APIRouter(prefix="/scores", tags=["Scores"])


# Create Tournament
@router.post("/", response_model=scores.ScoreResponse)
def create_tournament(tournament: scores.ScoreCreate, db: Session = Depends(database.get_db)):
    new_tournament = s.Score(**tournament.model_dump())
    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)
    return new_tournament

# Get All Tournaments
@router.get("/", response_model=list[scores.ScoreResponse])
def get_tournaments(db: Session = Depends(database.get_db)):
    return db.query(s.Score).all()

# Get Score by ID
@router.get("/{id}", response_model=scores.ScoreResponse)
def get_tournament(id: int, db: Session = Depends(database.get_db)):
    tournament = db.query(s.Score).filter(s.Score.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    return tournament

# Update Score
@router.put("/{id}", response_model=scores.ScoreResponse)
def update_tournament(id: int, updated: scores.ScoreCreate, db: Session = Depends(database.get_db)):
    tournament = db.query(s.Score).filter(s.Score.id == id).first()
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
    tournament = db.query(s.Score).filter(s.Score.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Score not found")
    db.delete(tournament)
    db.commit()
    return {"message": "Scores deleted successfully"}
