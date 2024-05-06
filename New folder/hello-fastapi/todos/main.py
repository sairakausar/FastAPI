import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_home():
    return {"hellosssss":"world"}

@app.get("/DAta")
def update_data():
    return {"update Data": "up"}
    
def start():
    uvicorn.run("todos.main:app", host="127.0.0.3", port="8081")