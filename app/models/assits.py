from sqlalchemy import (
    Column, Integer, ForeignKey
)
from sqlalchemy.orm import relationship
from ..db.database import Base
class Assist(Base):
    __tablename__ = "assists"

    id = Column(Integer,primary_key=True,index=True)
    player_id = Column(Integer,ForeignKey("player.id"),nullable=False,unique=True)

    #relationships
    player = relationship("Players",back_populates="assists")