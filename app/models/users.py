from models.base import Base
from sqlalchemy import Column, String, JSON, Integer, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    cities = relationship("City", secondary="user_cities_relations")


class UserCreate(BaseModel):
    username: str
    password: str
