from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.model import Todo
from app.schema.todo import TodoReturn, TodoCreate
from .auth import verify_token

router = APIRouter(prefix='/api/todo', tags=['todo'], dependencies=[Depends(verify_token)])


@router.get('', response_model=list[TodoReturn])
async def get_todos(index: int, size: int, db: Session = Depends(get_db)):
    return db.query(Todo).offset((index - 1) * size).limit(size).all()


@router.post('', response_model=TodoReturn, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_item = Todo(**todo.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get('/{id}', response_model=TodoReturn)
async def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Todo).filter(Todo.id == id).first()


@router.put('/{id}', response_model=TodoReturn)
async def update_todo_with_id(id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db.query(Todo).filter(Todo.id == id).update({'title': todo.title, 'is_complete': todo.is_complete})
    db.commit()
    return db.query(Todo).filter(Todo.id == id).first()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_by_id(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Todo).filter(Todo.id == id).first()
    db.delete(db_item)
    db.commit()
