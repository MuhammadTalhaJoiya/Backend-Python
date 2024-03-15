from fastapi import FastAPI,HTTPException
from sqlmodel import Field,SQLModel,create_engine,Session
from typing import Optional
from pydantic import BaseModel

# Todo class: This defines the structure of your Todo model using SQLModel. It represents a table in your database with fields id, content, and is_complete.
class Todo(SQLModel,table=True):
    id :Optional[int]=Field(default=None,primary_key=True)
    content:str
    is_complete:bool=Field(default=False)

# UserData class: This is a Pydantic model used for validating the data sent in the request body when creating a new todo item.
class UserData(BaseModel):
    content:str
    is_complete:bool=False

# db_url: This is the URL to your PostgreSQL database.
db_url='postgresql://neondb_owner:ucqGJyI0Ch8T@ep-late-firefly-a7k419pa.ap-southeast-2.aws.neon.tech/todo?sslmode=require'

# engine: This creates the database engine using SQLAlchemy.
engine=create_engine(db_url,echo=True)

# create_table function: This function is used to create the table corresponding to the Todo model in the database.
def create_table():
    SQLModel.metadata.create_all(engine)

# insert_data function: This function inserts data into the Todo table in the database.
def insert_data(content:str):
    with Session(engine) as session:
        data:Todo=Todo(content=content)
        session.add(data)
        session.commit()
        session.close()
app=FastAPI(
    title="Todo App Joiya"
)

@app.get('/')
def read_read():
    return {"messege":"Ramadhan Mubarak"}

# @app.post("/todo"): This is a route for creating a new todo item. It expects a JSON payload with content and is_complete fields.
@app.post("/todo")
def write_todo(userdata:UserData):
    if(userdata):
        if(len(userdata.content)!=0):
            insert_data(userdata.content)
        else:
            return {"messege":"type something"}
        return {"messege":"I am Post"}
    else:
        raise HTTPException(status_code=404,detail="Not found")
