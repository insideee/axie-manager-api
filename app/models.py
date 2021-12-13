from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    avatar = Column(String, nullable=False, server_default='default')
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    