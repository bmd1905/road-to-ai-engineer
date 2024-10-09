from typing import Dict

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(default="admin")
    password: str = Field(default="admin")


class FakeDB:

    # Simulated in-memory database
    users: Dict = {
        "admin": User(username="admin", password="admin"),
    }

    def add_user(self, user: User):
        print(f"Adding user: {user}")
        self.users[user.username] = user

    def get_user(self, username: str):  # Change parameter to username
        return self.users.get(username)  # Return user if exists, else None

    def close(self):
        print("Closing database connection...")  # Simulate closing


async def get_client():
    client = FakeDB()
    try:
        yield client
    finally:
        client.close()


app = FastAPI()


@app.post("/create_user")
async def create_user(user: User, client: FakeDB = Depends(get_client)):
    client.add_user(user)
    return {"user": user}


@app.get("/get_user/{username}")  # Use path parameter for username
async def get_user(username: str, client: FakeDB = Depends(get_client)):
    user = client.get_user(username)  # Get user by username
    if user is None:
        raise HTTPException(
            status_code=404, detail="User not found"
        )  # Raise error if not found
    return {"user": user}
