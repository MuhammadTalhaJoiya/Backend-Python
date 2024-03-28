# from fastapi import FastAPI,HTTPException
# from sqlmodel import Field,SQLModel,create_engine,Session
# from typing import Optional
# from pydantic import BaseModel

# # Todo class: This defines the structure of your Todo model using SQLModel. It represents a table in your database with fields id, content, and is_complete.
# class Todo(SQLModel,table=True):
#     id :Optional[int]=Field(default=None,primary_key=True)
#     content:str
#     is_complete:bool=Field(default=False)

# # UserData class: This is a Pydantic model used for validating the data sent in the request body when creating a new todo item.
# class UserData(BaseModel):
#     content:str=Field(nullable=False)
#     is_complete:bool=False

# # db_url: This is the URL to your PostgreSQL database.
# db_url='postgresql://neondb_owner:ucqGJyI0Ch8T@ep-late-firefly-a7k419pa.ap-southeast-2.aws.neon.tech/todo?sslmode=require'

# # engine: This creates the database engine using SQLAlchemy.
# engine=create_engine(db_url,echo=True)

# # create_table function: This function is used to create the table corresponding to the Todo model in the database.
# def create_table():
#     SQLModel.metadata.create_all(engine)

# # insert_data function: This function inserts data into the Todo table in the database.
# def insert_data(content:str):
#     with Session(engine) as session:
#         data:Todo=Todo(content=content)
#         session.add(data)
#         session.commit()
# app=FastAPI(
#     title="Todo App Joiya"
# )

# @app.get('/')
# def read_read():
#     return {"messege":"Ramadhan Mubarak"}

# # @app.post("/todo"): This is a route for creating a new todo item. It expects a JSON payload with content and is_complete fields.
# @app.post("/todo")
# def write_todo(userdata:UserData):
#     if(userdata):
#         if(len(userdata.content)!=0):
#             insert_data(userdata.content)
#         else:
#             return {"messege":"type something"}
#         return {"messege":"I am Post"}
#     else:
#         raise HTTPException(status_code=404,detail="Not found")


# main.py
from contextlib import asynccontextmanager
from typing import Union, Optional, Annotated
# from fastapi_neon import settings
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Depends

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


# only needed for psycopg 3 - replace postgresql
# with postgresql+psycopg in settings.DATABASE_URL
connection_string = "postgresql://neondb_owner:2AGKMaPvf8nr@ep-late-firefly-a7k419pa.ap-southeast-2.aws.neon.tech/todoapp?sslmode=require"


# recycle connections after 5 minutes
# to correspond with the compute scale down
engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="Hello World API with DB", 
    )

def get_session():
    with Session(engine) as session:
        yield session


@app.get("/") 
def read_root():
    return {"Hello": "Pakistan"}

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo


@app.get("/todos/", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
        todos = session.exec(select(Todo)).all()
        return todos

@app.put("/todos/{todo_id}",response_model=Todo)
def update_request(todo_:Todo,session:Annotated[Session,Depends(get_session)]):
    select_todo=session.exec(select(Todo).where(Todo.id==todo_.id)).one()
    select_todo.content=todo_.content
    session.add(select_todo)
    session.commit()
    session.refresh(select_todo)
    return select_todo

@app.delete("/todos/{id_number}",response_model=Todo)
def delete_request(todo_delete:Todo,session:Annotated[Session,Depends(get_session)]):
    delete_todo=session.exec(select(Todo).where(Todo.id==todo_delete.id)).first()
    session.delete(delete_todo)
    session.commit()
    return delete_todo