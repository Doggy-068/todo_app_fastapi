from fastapi import FastAPI
from app.router import todo
from app.database import model
from app.database.database import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='todo_app'
)

app.include_router(todo.router)
