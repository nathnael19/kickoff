from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TournamentBase(BaseModel):
    name: str
    year: int
    description: Optional[str] = None
    status: Optional[str] = "upcoming"

class TournamentCreate(TournamentBase):
    pass

class TournamentResponse(TournamentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

