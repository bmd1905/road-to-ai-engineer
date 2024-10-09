from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/items/", response_model=list[Item])
async def read_items():
    return [
        Item(name="Banh trung thu thap cam", price=45.0),
        Item(name="Banh trung thu dau xanh", price=40.0),
    ]
