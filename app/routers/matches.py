from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..models import matches as m
from ..schemas import matches
from ..db import database

router = APIRouter(prefix="/matches", tags=["Matches"])


# Create Match
@router.post("/", response_model=matches.MatchResponse)
def create_tournament(tournament: matches.MatchCreate, db: Session = Depends(database.get_db)):
    new_tournament = m.Match(**tournament.model_dump())
    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)
    return new_tournament

# Get All Match
@router.get("/", response_model=list[matches.MatchResponse])
def get_tournaments(db: Session = Depends(database.get_db)):
    return db.query(m.Match).all()

# Get Match by ID
@router.get("/{id}", response_model=matches.MatchResponse)
def get_tournament(id: int, db: Session = Depends(database.get_db)):
    tournament = db.query(m.Match).filter(m.Match.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    return tournament

# Update Match
@router.put("/{id}", response_model=matches.MatchResponse)
def update_tournament(id: int, updated: matches.MatchCreate, db: Session = Depends(database.get_db)):
    tournament = db.query(m.Match).filter(m.Match.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    for field, value in updated.dict().items():
        setattr(tournament, field, value)
    db.commit()
    db.refresh(tournament)
    return tournament

# Delete Match
@router.delete("/{id}")
def delete_tournament(id: int, db: Session = Depends(database.get_db)):
    tournament = db.query(m.Match).filter(m.Match.id == id).first()
    if not tournament:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    db.delete(tournament)
    db.commit()
    return {"message": "matches deleted successfully"}
