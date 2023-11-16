import os

from sqlalchemy import (Column, DateTime, Integer, Boolean, MetaData, String, Table, DateTime, ForeignKey,
                        create_engine)
from databases import Database

DATABASE_URL = "postgresql://postgres:1234@localhost/SquadStatDB"#os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

players = Table(
    "players",
    metadata,
    Column("steamid64", String(17), primary_key=True, index=True),
    Column("player_name", String(50), index=True, nullable=False),
    Column("email", String(100), unique=True, index=True, nullable=False),
    Column("total_kills", Integer),
    Column("total_deaths", Integer),
    Column("total_assists", Integer),
    Column("total_wins", Integer),
    Column("total_battles", Integer),
)

weapon_types = Table(
    "weapon_types",
    metadata,
    Column("weapon_id", Integer, primary_key=True, index=True),
    Column("weapon_name", String(50), index=True, nullable=False),
)

maps = Table(
    "maps",
    metadata,
    Column("map_id", Integer, primary_key=True, index=True),
    Column("map_name", String(50), index=True, nullable=False),
)

game_sessions = Table(
    "game_sessions",
    metadata,
    Column("session_id", Integer, primary_key=True, index=True),
    Column("player_id", String(17), ForeignKey("players.steamid64")),
    Column("map_id", Integer, ForeignKey("maps.map_id")),
    Column("session_date", DateTime),
    Column("total_kills", Integer),
    Column("total_deaths", Integer),
    Column("total_assists", Integer),
    Column("is_win", Boolean),
)

session_weapons = Table(
    "session_weapons",
    metadata,
    Column("session_id", Integer, ForeignKey("game_sessions.session_id"), primary_key=True),
    Column("weapon_id", Integer, ForeignKey("weapon_types.weapon_id"), primary_key=True),
    Column("kills", Integer),
)


# databases query builder
db = Database(DATABASE_URL)
