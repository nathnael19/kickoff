from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..models import matches as m
from ..schemas import matches
from ..db import database

router = APIRouter(prefix="/matches", tags=["Matches"])


# Create Match
@router.post("/", response_model=matches.MatchResponse)
def create_match(match: matches.MatchCreate, db: Session = Depends(database.get_db)):
    new_match = m.Match(**match.model_dump())
    db.add(new_match)
    db.commit()
    db.refresh(new_match)
    return new_match

# Get All Match
@router.get("/", response_model=list[matches.MatchResponse])
def get_matchs(db: Session = Depends(database.get_db)):
    return db.query(m.Match).all()

# Get Match by ID
@router.get("/{id}", response_model=matches.MatchResponse)
def get_match(id: int, db: Session = Depends(database.get_db)):
    match = db.query(m.Match).filter(m.Match.id == id).first()
    if not match:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    return match

# Update Match
@router.put("/{id}", response_model=matches.MatchResponse)
def update_match(id: int, updated: matches.MatchCreate, db: Session = Depends(database.get_db)):
    match = db.query(m.Match).filter(m.Match.id == id).first()
    if not match:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    for field, value in updated.dict().items():
        setattr(match, field, value)
    db.commit()
    db.refresh(match)
    return match

# Delete Match
@router.delete("/{id}")
def delete_match(id: int, db: Session = Depends(database.get_db)):
    match = db.query(m.Match).filter(m.Match.id == id).first()
    if not match:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Match not found")
    db.delete(match)
    db.commit()
    return {"message": "matches deleted successfully"}
