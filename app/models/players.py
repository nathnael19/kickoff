from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
    TIMESTAMP, JSON, Enum
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

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

    # Relationship
    team = relationship("Team", back_populates="players")

    def __repr__(self):
        return f"<Player(full_name={self.full_name}, position={self.position})>"

