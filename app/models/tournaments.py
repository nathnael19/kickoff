from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text,
    TIMESTAMP
)
from sqlalchemy.orm import relationship, declarative_base
from ..db import database


class Score(database.Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(Text)
    status = Column(String(20), default="upcoming", nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now)

    # Relationships
    teams = relationship("Team", back_populates="tournament", cascade="all, delete")
    matches = relationship("Match", back_populates="tournament", cascade="all, delete")

    def __repr__(self):
        return f"<Tournament(name={self.name}, year={self.year}, status={self.status})>"

