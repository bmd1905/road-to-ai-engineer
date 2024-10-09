from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from auth.schemas import User

router = APIRouter()


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get current user.

    :param current_user: Current user.
    :return: Current user.
    """
    return current_user
