# main.py

from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a root endpoint (GET request to '/')
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# You can add more endpoints if you like!
@app.get("/items/{item_id}")
async def read_item(item_id: int, query_param: str | None = None):
    if query_param:
        return {"item_id": item_id, "query_param": query_param}
    return {"item_id": item_id}