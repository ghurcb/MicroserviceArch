from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

import jwt


def _get_secret() -> str:
    secret = os.getenv("JWT_SECRET", "change_me")
    return secret


def _get_algorithm() -> str:
    return os.getenv("JWT_ALGORITHM", "HS256")


def decode_token(token: str) -> Dict[str, Any]:
    return jwt.decode(token, _get_secret(), algorithms=[_get_algorithm()])

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MIN", 30)))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, _get_secret(), algorithm=_get_algorithm())
    return encoded_jwt
