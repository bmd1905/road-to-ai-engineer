from pydantic import BaseModel


class UserBase(BaseModel):
    """User base schema"""

    name: str
    email: str


class UserCreate(UserBase):
    """User create schema"""

    pass


class UserUpdate(UserBase):
    """User update schema"""

    pass


class User(UserBase):
    """User schema"""

    id: int

    class Config:
        orm_mode = True
