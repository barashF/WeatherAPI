from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select
from models.cities import City
from models.users import User
from typing import Optional

class CityRepository:

    async def add_city(self, name: str, latitude: float, 
                       longitude: float, forecast: dict, session: Session) -> int:
        city = await session.execute(select(City).where(City.name == name, 
                                                   City.latitude == latitude, 
                                                   City.longitude == longitude))
        city_instance = city.scalar_one_or_none()
        if not city_instance:
            city_instance = City(name=name, latitude=latitude, 
                                 longitude=longitude, forecast=forecast)
            session.add(city_instance)
            await session.commit()
        return city_instance.id
    
    async def get_cities(self, session: Session) -> list[City]:
        result = await session.execute(select(City))
        return result.scalars().all()

    async def get_cities_by_user(self, user_id: int, session: Session) -> list[City]:
        result = await session.execute(select(User).where(User.id == user_id).options(joinedload(User.cities)))
        user = result.scalars().first()
        if user:
            return user.cities
        return []
    
    async def get_city_by_name(self, name: str, session: Session) -> Optional[City]:
        result = await session.execute(select(City).where(City.name == name))
        return result.scalars().first()