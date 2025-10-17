# Import all models so SQLAlchemy metadata knows about them
from .admin import Admin
from .tournaments import Tournament
from .teams import Team
from .players import Player
from .assists import Assist
from .goals import GoalRecord
from .matches import Match
from .scores import Score
