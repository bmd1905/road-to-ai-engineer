from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserDetails(BaseModel):
    full_name: str
    age: int | None = None


class User(BaseModel):
    id: int | None = None
    username: str
    details: UserDetails


# Updated fake database with nested structure
fake_db = [
    {
        "id": 0,
        "username": "Nam",
        "details": {
            "full_name": "Nam Nguyen",
            "age": 30,
        },
    },
    {
        "id": 1,
        "username": "Lan",
        "details": {
            "full_name": "Lan Tran",
            "age": 28,
        },
    },
]


@app.get("/get_user/{user_id}", response_model=User)
def get_user(user_id: int):
    return fake_db[user_id]


@app.post("/create_user", response_model=User)
def create_user(user: User):
    user.id = len(fake_db)
    fake_db.append(user)
    return user
