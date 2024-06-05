from typing import List

from app.models import Todo
from app.db import SessionLocal


def get_all_todos() -> List[Todo]:
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return todos


def create_todo(title: str) -> Todo:
    db = SessionLocal()
    new_todo = Todo(title=title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    db.close()
    return new_todo


def delete_todo(todo_id: int) -> bool:
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return True
    db.close()
    return False


def update_todo_completion(todo_id: int, completed: bool) -> bool:
    db = SessionLocal()
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        todo.completed = completed # type: ignore
        db.commit()
        return True
    db.close()
    return False