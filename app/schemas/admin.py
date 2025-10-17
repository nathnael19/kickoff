from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class AdminBase(BaseModel):
    username: str
    password: str


class AdminCreate(AdminBase):
    pass


class AdminResponse(AdminBase):
    id: int
    created_at: datetime