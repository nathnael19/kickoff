from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class Assist(Base):
    __tablename__ = "assists"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False, unique=True)

    # Relationships
    player = relationship("Player", back_populates="assists_records")
    goals = relationship("GoalRecord", back_populates="assist")
