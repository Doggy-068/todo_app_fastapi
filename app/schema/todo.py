from pydantic import BaseModel


class TodoReturn(BaseModel):
    id: int
    title: str
    is_complete: bool


class TodoCreate(BaseModel):
    title: str
    is_complete: bool
