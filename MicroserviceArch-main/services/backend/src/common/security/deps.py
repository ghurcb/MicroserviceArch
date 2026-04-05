from __future__ import annotations

from typing import Optional
from dataclasses import dataclass

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.security.jwt import decode_token
from src.infrastructure.db.deps import get_db
from src.infrastructure.db.models import User  # модель SQLAlchemy

bearer_scheme = HTTPBearer(auto_error=False)


@dataclass
class UserDTO:
    """
    DTO for User extracted from JWT token.
    This is NOT a database model.
    """
    id: int
    email: str
    username: Optional[str] = None


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> UserDTO:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    try:
        payload = decode_token(credentials.credentials)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    subject = payload.get("sub")
    user_id = payload.get("id")
    username = payload.get("username")

    if not subject:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload: missing sub")
    
    if user_id is None:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload: missing id")

    return UserDTO(id=int(user_id), email=subject, username=username)


async def get_current_user_model(
    current_user_dto: UserDTO = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Возвращает полную модель пользователя из БД."""
    user = await db.get(User, current_user_dto.id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
    