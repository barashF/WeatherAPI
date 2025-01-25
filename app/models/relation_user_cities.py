from models.base import Base
from sqlalchemy import Column, String, JSON, Integer, ForeignKey
from sqlalchemy.orm import relationship


class UserCitiesRelation(Base):
    __tablename__ = 'user_cities_relations'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), primary_key=True)