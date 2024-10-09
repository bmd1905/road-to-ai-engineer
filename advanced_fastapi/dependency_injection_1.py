from fastapi import FastAPI
from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(default="admin")
    password: str = Field(default="admin")


class FakeDB:
    def __init__(self):
        pass

    def add_user(self, user: User):
        pass

    def get_user(self, user: User):
        pass

app = FastAPI()

client = FakeDB()


@app.post("/create_user")
async def create_user(user: User):
    client.add_user(user)
    return {"user": user}


@app.get("/get_user")
async def get_user(user: User):
    client.get_user(user)
    return {"user": user}
