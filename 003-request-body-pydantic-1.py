from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {
        "id": 0,
        "username": "Nam",
    },
    {
        "id": 1,
        "username": "Lan",
    },
]


class User(BaseModel):
    id: int | None = None
    username: str


@app.get("/get_user/{user_id}")
def get_user(user_id: int):
    return fake_db[user_id]


@app.post("/post_user")
def post_user(user: User):
    user.id = len(fake_db)
    fake_db.append(user)
    return user


@app.put("/update_user/{user_id}")
def update_user(user_id: int, user: User):
    fake_db[user_id]["username"] = user.username
    return fake_db[user_id]


@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    del fake_db[user_id]
    return {"message": "User deleted successfully"}
