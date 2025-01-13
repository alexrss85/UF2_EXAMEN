from fastapi import FastAPI
from connection import conexio

conn = conexio()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}