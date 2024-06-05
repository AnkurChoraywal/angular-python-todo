from fastapi import FastAPI
from app.crud import get_all_todos, create_todo, delete_todo, update_todo_completion
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

ALLOWED_ORIGINS = [os.environ['ALLOWED_ORIGINS']]
APP_ROUTE = os.environ['APP_ROUTE']
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def rewrite_url(request, call_next):
    if request.url.path.startswith(APP_ROUTE):
        new_path = request.url.path.replace(APP_ROUTE, '')
        request.scope['path'] = new_path
    response = await call_next(request)
    return response

@app.get("/health")
async def hello():
    return {"message": "hello world"}

@app.get("/todos")
async def read_todos():
    return get_all_todos()


@app.post("/todos")
async def create_todo_item(title: str):
    return create_todo(title)


@app.delete("/todos/{todo_id}")
async def delete_todo_by_id(todo_id: int):
    if delete_todo(todo_id):
        return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}


@app.patch("/todos/{todo_id}")
async def update_todo_completion(todo_id: int, completed: bool):
    if update_todo_completion(todo_id, completed):
        return {"message": "Todo completion updated successfully"}
    return {"message": "Todo not found"}
 