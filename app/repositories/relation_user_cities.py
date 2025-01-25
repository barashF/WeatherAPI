from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import select
from models.cities import City
from models.users import User
from models.relation_user_cities import UserCitiesRelation


class UserCitiesRelationRepository:

    async def relation_city_with_user(self, user_id: int, city_id: int, session: Session) -> None:
        user = await session.execute(select(User).where(User.id == user_id))
        user = user.scalars().first()
        city = await session.execute(select(City).where(City.id == city_id))
        city = city.scalars().first()
        if user and city:
            new_user_city = UserCitiesRelation(user_id=user_id, city_id=city_id)
            session.add(new_user_city)
            await session.commit()