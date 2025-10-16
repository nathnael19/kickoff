from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
    TIMESTAMP, JSON, Enum
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"), unique=True, nullable=False)
    home_score = Column(Integer, default=0)
    away_score = Column(Integer, default=0)
    goal_scorers = Column(JSONB)
    yellow_cards = Column(JSONB)
    red_cards = Column(JSONB)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    match = relationship("Match", back_populates="score")

    def __repr__(self):
        return f"<Score(match_id={self.match_id}, {self.home_score}-{self.away_score})>"
