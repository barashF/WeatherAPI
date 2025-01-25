from repositories import cities as cities_repository
from repositories import users as users_repository
from repositories import relation_user_cities as relation_user_cities_repository
from repositories import forecast
from services import cities as cities_service, users as users_service
from services import auth
from services import relation_user_cities as relation_user_cities_service
from services import update_forecast

city_repository = cities_repository.CityRepository()
city_service = cities_service.CityService(city_repository)

user_repository = users_repository.UserRepository()
user_service = users_service.UserServise(user_repository)

auth_service = auth.AuthService(user_repository)

relation_user_city_repository = relation_user_cities_repository.UserCitiesRelationRepository()
relation_user_city_service = relation_user_cities_service.UserCitiesRelationService(relation_user_city_repository)

forecast_repository = forecast.ForecastRepository()
forecast_service = update_forecast.ForecastService(forecast_repository)

def get_city_service() -> cities_service.CityService:
    return city_service

def get_user_service() -> users_service.UserServise:
    return user_repository

def get_auth_service() -> auth.AuthService:
    return auth_service

def get_relation_user_city_service() -> relation_user_cities_service.UserCitiesRelationService:
    return relation_user_city_service

def get_forecast_service() -> update_forecast.ForecastService:
    return forecast_service