from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from repositories.users import UserRepository


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def verify_password(self, password, hashed_password):
        return pwd_context.verify(password, hashed_password)
    
    def get_hash_password(self, password):
        return pwd_context.hash(password)

    async def authenticate_user(self, username: str, password: str, session: Session):
        user = await self.repository.get_user_by_username(session, username)
        if not user or not self.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return user