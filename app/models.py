from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
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
    slp_total = Column(Integer, nullable=False)
    slp_yesterday = Column(Integer, nullable=False)
    slp_total = Column(Integer, nullable=False)
    winrate = Column(Integer, nullable=False)
    average = Column(Integer, nullable=False)
    elo = Column(Integer, nullable=False)
    scholar_earns_percent = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    