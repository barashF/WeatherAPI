import asyncio
from fastapi import Depends
from sqlalchemy.orm import Session
from services.weather import get_weather
from database import SessionLocal
from repositories.cities import CityRepository
from repositories.forecast import ForecastRepository


class ForecastService:
    def __init__(self, repository: ForecastRepository):
        self.repository = repository

    async def update_forecast(self):
        while True:
            session = SessionLocal()
            cities = await self.repository.get_cities(session)

            for city in cities:
                try:
                    forecast = await get_weather(latitude=city.latitude, longitude=city.longitude)
                    await self.repository.update_forecast(city.id, forecast, session)

                except:
                    print(f'Failed update forecast for {city.name}')
        
            await asyncio.sleep(900)
        



