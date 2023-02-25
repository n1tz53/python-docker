from fastapi import FastAPI

app = FastAPI()

@app.get("/{a}/{b}")
async def root(a: int, b: int):
    return a * b
