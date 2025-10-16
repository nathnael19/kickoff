from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,Boolean,
    TIMESTAMP, JSON, Enum
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class GoalRecord(Base):
    __tablename__ = "goals"

    id = Column(Integer,primary_key=True,index=True)
    match_id = Column(Integer,ForeignKey("matches.id",ondelete="CASCADE"),unique=True,nullable=False)
    player_id = Column(Integer,ForeignKey("players.id",ondelete="CASCADE"),unique=True,nullable=False)
    assist_id = Column(Integer,ForeignKey("assists.id",ondelete="CASCADE"),unique=True,nullable=True)
    minute = Column(Integer)
    is_own_goal = Column(Boolean,default=False)
    created_at = Column(TIMESTAMP,default=datetime.now)

    # Relationship
    match = relationship("GoalRecord", back_populates="goals")
    player = relationship("Players",back_populates="goals")
    assist = relationship("Assist",back_populates="goals")