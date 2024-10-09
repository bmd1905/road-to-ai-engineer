from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .config import settings
from .dependencies import fake_users_db
from .exceptions import credentials_exception
from .schemas import Token
from .service import authenticate_user
from .utils import create_access_token

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Authenticate user and return access token.

    :param form_data: Form data containing username and password.
    :return: Access token.
    """
    # Authenticate user
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)

    # Raise exception if user is not authenticated
    if not user:
        raise credentials_exception

    # Create access token expiration time
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)

    # Create access token
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # Return access token
    return Token(access_token=access_token, token_type="bearer")
