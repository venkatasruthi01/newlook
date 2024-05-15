from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

db = []

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/items/", response_model=List[Item])
def read_items():
    return db

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, db_item in enumerate(db):
        if db_item.id == item_id:
            db[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            del db[index]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
