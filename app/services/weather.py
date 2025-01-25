import httpx


API_URL = "https://api.open-meteo.com/v1/forecast"


async def get_weather(latitude: float, longitude: float):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch weather data: {response.text}")
        
        data = response.json()
        if "current_weather" not in data:
            raise HTTPException(status_code=500, detail="Invalid response from weather API")
        
        current_weather = data["current_weather"]
        return {
            "temperature": current_weather.get("temperature"),
            "windspeed": current_weather.get("windspeed"),
            "pressure": current_weather.get("pressure")
        }