from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.router import auth, todo, file, ws, graphql
from app.database import model
from app.database.database import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='todo_app'
)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/file', StaticFiles(directory='file'), name='file')

app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(file.router)
app.include_router(ws.router)
app.include_router(graphql.router, include_in_schema=False)
