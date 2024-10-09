from fastapi import FastAPI

from auth.router import router as auth_router
from users.routes import router as user_router

app = FastAPI(
    title="FastAPI Auth Example",
    description="This is a simple auth example using FastAPI",
    version="0.1.0",
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    """
    Root endpoint.

    :return: Welcome message.
    """
    return {"message": "Welcome to the FastAPI Auth Example"}
