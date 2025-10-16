from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MatchBase(BaseModel):
    tournament_id: int
    home_team_id: int
    away_team_id: int
    date_time: datetime
    location: str
    round: str
    status: Optional[str] = "scheduled"

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


