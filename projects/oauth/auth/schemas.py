from pydantic import BaseModel


class Token(BaseModel):
    """Token schema."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data schema."""

    username: str | None = None


class User(BaseModel):
    """User schema."""

    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    """User in database schema."""

    hashed_password: str
