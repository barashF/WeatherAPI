from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.cities import CityCreate
from services.weather import get_weather
from sqlalchemy.orm import Session
from depends import get_auth_service, get_city_service, get_relation_user_city_service
from database import get_session


security = HTTPBasic()
router = APIRouter()


@router.post('/users/{user_id}/add_city')
async def add_city(user_id: int, city: CityCreate, 
                    credentials: HTTPBasicCredentials = Depends(security), 
                    session: Session = Depends(get_session)):
    user = await get_auth_service().authenticate_user(credentials.username, credentials.password, session)
    if user.id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action")
    
    existing_city = await get_city_service().get_city_by_name(city.name, session)
    if existing_city:
        await get_relation_user_city_service().create_relation_user_with_cities(user_id, existing_city.id, session)
    else:
        forecast = await get_weather(city.latitude, city.longitude)
        city_id = await get_city_service().add_city(city.name, city.latitude, city.longitude, forecast, session)
        await get_relation_user_city_service().create_relation_user_with_cities(user_id, city_id, session)
    return {"message": "success"}

@router.get("/users/{user_id}/cities/{city_name}/weather")
async def get_city_weather(user_id: int, city_name: str, temperature: 
                           bool = False, humidity: bool = False, 
                           wind_speed: bool = False, precipitation: bool = False,
                           credentials: HTTPBasicCredentials = Depends(security), 
                           session: Session = Depends(get_session)):
    user = await get_auth_service().authenticate_user(credentials.username, credentials.password, session)
    if user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    
    city = await get_city_service().get_city_by_name(city_name, session)
    if not city or city not in await get_city_service().get_cities_by_user(user_id, session):
        raise HTTPException(status_code=404, detail="City not found.")

    forecast = city.forecast
    response = {}
    if temperature:
        response["temperature"] = forecast.get("temperature")
    if humidity:
        response["humidity"] = forecast.get("humidity")
    if wind_speed:
        response["wind_speed"] = forecast.get("windspeed")
    if precipitation:
        response["precipitation"] = forecast.get("precipitation")
    return response