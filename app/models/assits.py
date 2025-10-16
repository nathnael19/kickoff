from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
    TIMESTAMP, JSON, Enum
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class Assist(Base):
    __tablename__ = "assists"

    id = Column(Integer,primary_key=True,index=True)
    player_id = Column(Integer,ForeignKey("player.id"),nullable=False,unique=True)

    #relationships
    player = relationship("Players",back_populates="assists")