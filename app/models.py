from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    avatar = Column(String, nullable=False, server_default='default')
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    account = relationship("Account")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Account(Base):
    __tablename__ = 'account'
    
    id = Column(Integer, primary_key=True, nullable=False)
    ronin_address = Column(String, unique=True, nullable=False)
    player_name = Column(String, nullable=False)
    slp_total = Column(Integer)
    slp_yesterday = Column(Integer)
    slp_today = Column(Integer)
    winrate = Column(Integer)
    average = Column(Integer)
    elo = Column(Integer)
    scholar_earns_percent = Column(Integer, nullable=False)
    axies = relationship('Axie')
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Axie(Base):
    __tablename__ = 'axie'
    
    id = Column(Integer, primary_key=True, nullable=False)
    market_id = Column(String, nullable=False)
    name = Column(String, unique=True, nullable=False)
    stage = Column(Integer, nullable=False)
    class_ = Column(String, nullable=False)
    breedCount = Column(Integer, nullable=False)
    image = Column(String, nullable=False)
    banned = Column(Boolean, nullable=False)
    parts = Column(JSON, nullable=False)
    account_id = Column(Integer, ForeignKey('account.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    