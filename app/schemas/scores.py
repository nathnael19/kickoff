from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ScoreBase(BaseModel):
    match_id: int
    home_score: Optional[int] = 0
    away_score: Optional[int] = 0
    winner_team_id: int
    # goal_scorers: Optional[list] = None
    # yellow_cards: Optional[list] = None
    # red_cards: Optional[list] = None

class ScoreCreate(ScoreBase):
    pass

class ScoreResponse(ScoreBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True
