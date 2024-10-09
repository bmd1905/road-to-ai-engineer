from fastapi import FastAPI

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


@app.get("/get_user")
def get_user(user_id: int):
    return fake_db[user_id]


@app.post("/post_user")
def post_user(username: str):
    new_user = {"id": len(fake_db), "username": username}
    fake_db.append(new_user)
    return new_user


@app.put("/update_user")
def update_user(user_id: int, username: str):
    fake_db[user_id]["username"] = username
    return fake_db[user_id]


@app.delete("/delete_user")
def delete_user(user_id: int):
    del fake_db[user_id]
    return {"message": "User deleted successfully"}
