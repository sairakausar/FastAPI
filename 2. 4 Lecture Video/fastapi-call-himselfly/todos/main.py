import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_home():
    return {"read_me": "world"}

def start():
    uvicorn.run("todos.main:app" , host="127.0.0.5", port="9004")



