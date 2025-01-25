from models.base import Base
from sqlalchemy import Column, String, JSON, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    forecast = Column(JSON, nullable=True)
    users = relationship("User", secondary="user_cities_relations")


class CityCreate(BaseModel):
    name: str
    latitude: float
    longitude: float