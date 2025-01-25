from sqlalchemy.orm import Session 
from sqlalchemy import select
from models.users import User
from typing import Optional


class UserRepository:

    async def add_user(self, username: str, password: str, session: Session) -> Optional[int]:
        result = await session.execute(select(User).where(User.username == username))
        if result.scalar():
            return None
        user = User(username=username, password=password)
        session.add(user)
        await session.commit()
        return user.id
    
    async def get_user_by_username(self, session: Session, username: str) -> Optional[User]:
        result = await session.execute(select(User).where(User.username == username))
        return result.scalars().first()