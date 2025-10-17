from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class GoalBase(BaseModel):
    match_id:int
    player_id:int
    assist_id:int
    minute:int
    is_own_goal: Optional[bool] = False


class GoalCreate(GoalBase):
    pass


class GoalResponse(GoalBase):
    id:int
    created_at:datetime
