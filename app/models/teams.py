from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from ..db.database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    logo_url = Column(Text)
    played = Column(Integer, default=0)
    won = Column(Integer, default=0)
    lost = Column(Integer, default=0)
    drawn = Column(Integer, default=0)
    gf = Column(Integer, default=0)
    ga = Column(Integer, default=0)
    gd = Column(Integer, default=0)
    points = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    tournament = relationship("Tournament", back_populates="teams")
    players = relationship("Player", back_populates="team", cascade="all, delete")
    home_matches = relationship("Match", back_populates="home_team", foreign_keys="[Match.home_team_id]")
    away_matches = relationship("Match", back_populates="away_team", foreign_keys="[Match.away_team_id]")
    scores = relationship("Score", back_populates="winner")
