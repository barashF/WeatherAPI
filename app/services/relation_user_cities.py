from repositories.relation_user_cities import UserCitiesRelationRepository
from sqlalchemy.orm import Session


class UserCitiesRelationService:

    def __init__(self, repository: UserCitiesRelationRepository):
        self.repository = repository

    async def create_relation_user_with_cities(self, user_id: int, 
                                               city_id: int, session: Session) -> None:
        await self.repository.relation_city_with_user(user_id, city_id, session)