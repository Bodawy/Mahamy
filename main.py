from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []

@app.get("/")
async def read_root():
	return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
	return {"item_id": item_id, "q": q}


