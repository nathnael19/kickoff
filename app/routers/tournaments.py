from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import tournaments as tm
from ..schemas import tournaments

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

def get_db():
    pass

# Create Tournament
@router.post("/", response_model=tournaments.TournamentResponse)
def create_tournament(tournament: tournaments.TournamentCreate, db: Session = Depends(get_db)):
    new_tournament = tm.Tournament(**tournament.model_dump())
    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)
    return new_tournament

# Get All Tournaments
@router.get("/", response_model=list[tournaments.TournamentResponse])
def get_tournaments(db: Session = Depends(get_db)):
    return db.query(tm.Tournament).all()

# Get Tournament by ID
@router.get("/{id}", response_model=tournaments.TournamentResponse)
def get_tournament(id: int, db: Session = Depends(get_db)):
    tournament = db.query(tm.Tournament).filter(tm.Tournament.id == id).first()
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournament

# Update Tournament
@router.put("/{id}", response_model=tournaments.TournamentResponse)
def update_tournament(id: int, updated: tournaments.TournamentCreate, db: Session = Depends(get_db)):
    tournament = db.query(tm.Tournament).filter(tm.Tournament.id == id).first()
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    for field, value in updated.dict().items():
        setattr(tournament, field, value)
    db.commit()
    db.refresh(tournament)
    return tournament

# Delete Tournament
@router.delete("/{id}")
def delete_tournament(id: int, db: Session = Depends(get_db)):
    tournament = db.query(tm.Tournament).filter(tm.Tournament.id == id).first()
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    db.delete(tournament)
    db.commit()
    return {"message": "Tournament deleted successfully"}
