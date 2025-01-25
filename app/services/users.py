from repositories.users import UserRepository
from models.users import User
from typing import Optional
from sqlalchemy.orm import Session

class UserServise:

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository
    
    async def get_user_by_username(self, session: Session, username: str) -> Optional[User]:
        result = await self.repository.get_user_by_username(session, username)
        return result
    
    async def add_user(self, username: str, password: str, session: Session) -> Optional[int]:
        result = self.repository.add_user(username, password, session)
        return result