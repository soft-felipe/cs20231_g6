from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from fastapi import Depends, HTTPException, status
from jose import jwt

from schemas import User, UserCreate
from services import authenticate_user, get_user_by_username


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
            )
        user = await get_user_by_username(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )
        return user
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
        )
    return current_user


async def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient privileges",
        )
    return current_user


async def get_current_active_user_optional(
    current_user: User = Depends(get_current_user),
) -> User:
    return current_user


async def get_current_user_optional(
    token: str = Depends(oauth2_scheme),
) -> User:
    if token is not None:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication token",
                )
            user = await get_user_by_username(username)
            if user is not None:
                return user
        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
            )
    return None


async def get_current_active_superuser_optional(
    current_user: User = Depends(get_current_user_optional),
) -> User:
    if current_user is not None and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient privileges",
        )
    return current_user


async def get_current_active_user_or_superuser_optional(
    current_user: User = Depends(get_current_user_optional),
) -> User:
    if current_user is not None and not current_user.is_active and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
        )
    return current_user


async def get_current_user_create(
    user: UserCreate,
) -> User:
    return User(username=user.username, password=user.password)
