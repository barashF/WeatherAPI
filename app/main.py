from fastapi import FastAPI
import asyncio
from routers import weather, cities, users
from depends import get_forecast_service
from database import init_session

app = FastAPI()

app.include_router(weather.router)
app.include_router(cities.router)
app.include_router(users.router)

@app.on_event("startup")
async def startup_event():
    await init_session()
    asyncio.create_task(get_forecast_service().update_forecast())

@app.get("/")
async def read_root():
    return {"Hello": "World"}