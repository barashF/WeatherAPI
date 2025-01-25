from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select
from models.cities import City
from models.users import User
from typing import Optional


class ForecastRepository:

    async def update_forecast(self, city_id: int, forecast: dict, db: Session):
        city = await db.execute(select(City).where(City.id == city_id))
        city = city.scalars().first()
        if city:
            city.forecast = forecast
            await db.commit()
    
    async def get_cities(self, session: Session) -> list[City]:
        result = await session.execute(select(City))
        return result.scalars().all()