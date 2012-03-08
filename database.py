from sqlalchemy import Integer, String, DateTime, Boolean, Date, PickleType
from sqlalchemy import Column, ForeignKey
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, relationship, backref
import datetime

import config

Base = declarative_base()
engine = create_engine(config.sqlite_db, echo=True)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    wot_id = Column(Integer, index=True)
    region = Column(String, index=True)
    clan_id = Column(Integer, ForeignKey('clans.id'), index=True)
    enrolled = Column(Date)
    active = Column(Boolean)
    #url = column_property(
        # TODO
    #)


class VehicleData(Base):
    __tablename__ = 'vehicles'
    id = Column(String, primary_key=True) # from url
    name = Column(String) # printable
    type_id = Column(Integer) # type table is hardcoded ?
    tier = Column(Integer)
    is_top = Column(Boolean)
    

class Updates(Base):
    __tablename__ = 'updates'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), index=True)
    time = Column(DateTime, index=True)
    total = Column(Integer)
    wins = Column(Integer)
    defeats = Column(Integer)
    kills = Column(Integer)
    
    #@hybrid_property
    #def ratio
    


class Tank(Base):
    __tablename__ = 'tanks'
    player_id = Column(Integer, ForeignKey('vehicles.id'), index=True, primary_key=True)
    tank_id = Column(String, ForeignKey('players.id'), primary_key=True)
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
    region = Column(String)
    name = Column(String)
    full_name = Column(String)
    description = Column(String)
    
    #url = column_property(
        # TODO
    #)
    
    def __init__(self, url):
        pass # TODO
        

    
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, index=True)
    message_id = Column(Integer, ForeignKey('messages.id'), default=None)
    clan_id = Column(Integer, ForeignKey('clans.id'), default=None)
    dictionary = Column(PickleType)
    
    
class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)