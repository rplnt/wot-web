from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
engine = create_engine(sqlite_db, echo=True)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    wot_id = Column(String)
    region_id = Column(Integer, ForeignKey('regions.id'))
    clan_id = Column(Integer, ForeignKey('clans.id'))
    enrolled = Column(Date)
    
    def __init__(self, name, wot_id, region_id, clan_id, enrolled):
        self.name = name
        self.wot_id = wot_id
        self.region_id = region_id
        self.clan_id = clan_id
        self.enrolled = datetime.date.today()


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(String, primary_key=True) # from url
    name = Column(String) # printable
    type_id = Column(Integer) # type table is hardcoded ?
    tier = Column(Integer)
    is_top = Column(Boolean)
    
    def __init__(self, id, name, type_id, tier, is_top):
        self.id = id
        self.name = name
        self.type_id = type_id
        self.tier = tier
        self.is_top = is_top
    

class Updates(Base):
    __tablename__ = 'updates'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    time = Column(DateTime)
    total = Column(Integer)
    wins = Column(Integer)
    defeats = Column(Integer)
    kills = Column(Integer)
    
    def __init__(self, player_id, time, total, wins, defeats, kills):
        self.player_id = player_id
        self.time = time
        self.total = total
        self.wins = wins
        self.defeats = defeats
        self.kills = kills


class Tank(Base):
    __tablename__ = 'tanks'
    player_id = Column(Integer, ForeignKey('vehicles.id'))
    tank_id = Column(String, ForeignKey('platers.id'))
    total = Column(Integer)
    wins = Column(Integer)
    updated = Column(Date) # == last played
    

class Clan(Base):
    id = Column(Integer, primary_key=True)
    #region = Column(String)
    name = Column(String)