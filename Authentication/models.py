from sqlalchemy import Column, DateTime, Integer, String 
from sqlalchemy.sql import func 

from db_config import Base 

# Models define the database schema. Alembic can use them to generate migrations automatically via alembic revision --autogenerate.
class Post(Base):
    __tablename__ = "post"
    
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now() ) #automatically sets timestamp when inserted.
    
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String(255))