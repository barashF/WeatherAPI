from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_session
from depends import get_auth_service, get_user_service
from models.users import UserCreate


router = APIRouter()


@router.post('/register', response_model=dict)
async def register(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = get_auth_service().get_hash_password(user.password)
    user_id = await get_user_service().add_user(user.username, hashed_password, session)    
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username already exists.")
    return {"id": user_id}
