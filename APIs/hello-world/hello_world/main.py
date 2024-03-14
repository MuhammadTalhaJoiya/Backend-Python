# fastapi_neon/main.py

from fastapi import FastAPI

app = FastAPI(title="Hello World API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://localhost:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items")
# def read_items():
#     return {"Item":"skjd"}
# items:list=[{"name":"Talha"},{"name":"joiya"},{"name":"hamza"},{"name":"umer"},{"name":"ali"},{"name":"yusuf"}]
# @app.get("/items/")
# def query(skip:int=1,limit:int=10):
#     return items[skip:limit]

# Optional Query Parameter
from typing import Union
@app.get("/items/{item_id}")
def itemfunc(item_id:int,q:str|None=None):
    messege:dict={"Messege":item_id}
    if(q):
        messege.update({"qsas":q})
    return messege