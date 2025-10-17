from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class AssistBase(BaseModel):
    player_id:int


class AssistCreate(AssistBase):
    pass


class AssistResponse(AssistBase):
    id: int