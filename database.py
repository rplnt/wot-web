from sqlalchemy import Integer, String, DateTime, Boolean, Date, PickleType
from sqlalchemy import Column, ForeignKey
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property
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
    url = column_property(
        # TODO
    )
    
    
    def __init__(self, name, wot_id, region_id, clan_id, enrolled):
        self.name = name
        self.wot_id = wot_id
        self.region_id = region_id
        self.clan_id = clan_id
        self.enrolled = datetime.date.today()


class VehicleData(Base):
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
    
    #@hybrid_property
    #def ratio
    
    
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
    
    def __init__(self, player_id, tank_id, total, wins):
        self.player_id = player_id
        self.tank_id = tank_id
        self.total = total
        self.wins = wins
        self.updated = datetime.date.today()

    
class Clan(Base):
    __tablename__ = 'clans'
    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey('regions.id'))
    name = Column(String)
    url = Column(String)
    
    def __init__(self, url):
        pass # TODO
        


class Region(Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    shortname = Column(String)
    base_url = Column(String)
    
    
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    message_id = Column(Integer, ForeignKey('messages.id'))
    dictionary = Column(PickleType)
    
    
class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(String)