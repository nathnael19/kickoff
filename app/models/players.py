from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from ..db.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100), nullable=False)
    position = Column(String(50))
    jersey_number = Column(Integer)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    yellow_cards = Column(Integer, default=0)
    red_cards = Column(Integer, default=0)
    photo_url = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    team = relationship("Team", back_populates="players")
    assists_records = relationship("Assist", back_populates="player", cascade="all, delete")
    goals_records = relationship("GoalRecord", back_populates="player", cascade="all, delete")
