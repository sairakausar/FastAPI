from fastapi import FastAPI
import uvicorn 

app = FastAPI

@app.get("/")
def read_home():
    return {"Hello" : "World"}

