from fastapi import FastAPI
from sqlmodel import Field,SQLModel,create_engine
from typing import Optional


class Todo(SQLModel,Table=True):
    id :Optional[int]=Field(default=None,primary_key=True)
    content:str
    is_complete:bool=Field(default=False)

db_url='postgresql://saddsaknd:nVxZd5voqNj0@ep-late-firefly-a7k419pa.ap-southeast-2.aws.neon.tech/todoapp?sslmode=require'
engine=create_engine(db_url,echo=True)

SQLModel.metadata.create_all(engine)

app=FastAPI(
    title="klasdj"
)

@app.get('/')
def read_read():
    return {"messege":"Ramadhan Mubarak"}