from typing import Optional

from .schemas import UserInDB
from .utils import verify_password


def authenticate_user(db, username: str, password: str) -> Optional[UserInDB]:
    """
    Authenticate user.

    :param db: Database.
    :param username: Username.
    :param password: Password.
    :return: User if authenticated, None otherwise.
    """
    user = db.get(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
