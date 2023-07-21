from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.router import auth, todo, ws
from app.database import model
from app.database.database import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='todo_app'
)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(ws.router)
