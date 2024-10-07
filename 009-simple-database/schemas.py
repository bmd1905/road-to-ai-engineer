from pydantic import BaseModel


class UserBase(BaseModel):
    """User base schema"""

    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
