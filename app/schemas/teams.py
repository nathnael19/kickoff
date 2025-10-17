from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TeamBase(BaseModel):
    name: str
    department: str
    logo_url: Optional[str] = None
    played: Optional[int] = 0
    lost: Optional[int] = 0
    drawn: Optional[int] = 0
    won: Optional[int] = 0
    gf: Optional[int] = 0
    ga: Optional[int] = 0
    gd: Optional[int] = 0
    points: Optional[int] = 0
    tournament_id: int

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
