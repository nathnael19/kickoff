from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..models import players as s
from ..schemas import players
from ..db import database
from typing import Optional

router = APIRouter(prefix="/players", tags=["Players"])

# Get All Player
@router.get("/", response_model=list[players.PlayerResponse])
def get_players(db: Session = Depends(database.get_db),search:Optional[str]=""):
    return db.query(s.Player).filter(s.Player.full_name.contains(search)).all()



# Create Player
@router.post("/", response_model=players.PlayerResponse)
def create_Player(player: players.PlayerCreate, db: Session = Depends(database.get_db)):
    new_player = s.Player(**player.model_dump())
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player


# Get Player by ID
@router.get("/{id}", response_model=players.PlayerResponse)
def get_Player(id: int, db: Session = Depends(database.get_db)):
    player = db.query(s.Player).filter(s.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    return player

# Update Player
@router.put("/{id}", response_model=players.PlayerResponse)
def update_Player(id: int, updated: players.PlayerCreate, db: Session = Depends(database.get_db)):
    player = db.query(s.Player).filter(s.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    for field, value in updated.dict().items():
        setattr(player, field, value)
    db.commit()
    db.refresh(player)
    return player

# Delete Player
@router.delete("/{id}")
def delete_Player(id: int, db: Session = Depends(database.get_db)):
    player = db.query(s.Player).filter(s.Player.id == id).first()
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    db.delete(player)
    db.commit()
    return {"message": "players deleted successfully"}
