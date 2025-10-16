from datetime import datetime
from sqlalchemy import (
    Column, Integer, String,
    TIMESTAMP
)
from ..db.database import Base

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP,default=datetime.now)
