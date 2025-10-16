from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, ForeignKey,
    TIMESTAMP
)
from sqlalchemy.orm import relationship
from ..db.database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id", ondelete="CASCADE"), nullable=False)
    home_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    away_team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    date_time = Column(TIMESTAMP, nullable=False)
    location = Column(String(150), nullable=False)
    round = Column(String(50), nullable=False)
    status = Column(String(20), default="scheduled", nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    tournament = relationship("Tournament", back_populates="matches")
    home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")
    score = relationship("Score", back_populates="match", uselist=False, cascade="all, delete")

    def __repr__(self):
        return f"<Match({self.home_team_id} vs {self.away_team_id}, status={self.status})>"

