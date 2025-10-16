from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TeamBase(BaseModel):
    name: str
    department: str
    logo_url: Optional[str] = None
    tournament_id: int

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
