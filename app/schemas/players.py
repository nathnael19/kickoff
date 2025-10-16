from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class PlayerBase(BaseModel):
    full_name: str
    position: Optional[str] = None
    jersey_number: int
    team_id: int
    goals: Optional[int] = 0
    assists: Optional[int] = 0
    yellow_cards: Optional[int] = 0
    red_cards: Optional[int] = 0
    photo_url: Optional[str] = None

class PlayerCreate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
