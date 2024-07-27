from fastapi import FastAPI
from pydantic import BaseModel

# Pydantic is a Python library that helps you define data structures (models) by using Python type hints. 
# It automatically validates data against these models, ensuring data integrity and consistency.

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item