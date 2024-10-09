from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from .config import settings
from .exceptions import credentials_exception
from .schemas import TokenData, User, UserInDB

# OAuth2PasswordBearer is a FastAPI dependency that provides OAuth2 authentication.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# In-memory "database" (move to a proper database in production)
fake_users_db = {
    "bmd": UserInDB(
        username="bmd",
        full_name="bmd1905",
        email="bmd@example.com",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        disabled=False,
    )
}


def get_user(db, username: str) -> UserInDB | None:
    """
    Get user from database.

    :param db: Database.
    :param username: Username.
    :return: User if found, None otherwise.
    """
    return db.get(username)


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Get current user from token.

    :param token: Token.
    :return: Current user.
    """
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = (
        get_user(fake_users_db, username=token_data.username)
        if token_data.username
        else None
    )
    if user is None:
        raise credentials_exception
    return user
