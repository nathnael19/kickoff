from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from ..db.database import Base

class GoalRecord(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"), nullable=False)
    assist_id = Column(Integer, ForeignKey("assists.id", ondelete="CASCADE"), nullable=True)
    minute = Column(Integer)
    is_own_goal = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    match = relationship("Match", back_populates="goals")
    player = relationship("Player", back_populates="goals_records")
    assist = relationship("Assist", back_populates="goals")
