from fastapi import APIRouter, HTTPException, Query, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from services.weather import get_weather as get_open_meteo
from sqlalchemy.orm import Session


security = HTTPBasic()
router = APIRouter()


@router.get('/weather')
async def get_weather(
                       latitude: float = Query(..., ge=-90, le=90), 
                       longitude: float = Query(..., ge=-180, le=180)):
    # user = authenticate_user(db, credentials.username, credentials.password)
    try:
        weather = await get_open_meteo(latitude, longitude)
        return {
            'temperature': weather['temperature'],
            'wind_speed': weather['windspeed'],
            'pressure': weather['pressure']
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))