from repositories.cities import CityRepository
from models.cities import City
from sqlalchemy.orm import Session
from typing import Optional


class CityService:

    def __init__(self, repository: CityRepository):
        self.repository = repository

    async def add_city(self, name: str, latitude: float, 
                       longitude: float, forecast: dict, session: Session) -> int:
        result = await self.repository.add_city(name, latitude, longitude, 
                                                forecast, session)
        return result
    
    async def get_cities(self, session: Session) -> list[City]:
        result = await self.repository.get_cities(session)
        return result
    
    async def get_cities_by_user(self, user_id: int, session: Session) -> list[City]:
        result = await self.repository.get_cities_by_user(user_id, session)
        return result
    
    async def get_city_by_name(self, name: str, session: Session) -> Optional[City]:
        result = await self.repository.get_city_by_name(name, session)
        return result