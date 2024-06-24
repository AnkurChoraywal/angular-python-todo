from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.crud import get_all_todos, create_todo, delete_todo, update_todo_completion
import os
import sys

app = FastAPI()

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

def get_file(file):
    if hasattr(sys, '_MEIPASS'):
        print('binary mode: reading from _MEIPASS temp directory')
        return os.path.join(sys._MEIPASS, 'data', file)
    print('source code mode: reading from filesystem')
    return os.path.join(os.path.dirname(__file__), file)

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
async def update_todo(todo_id: int, completed: bool):
    if update_todo_completion(todo_id, completed):
        return {"message": "Todo completion updated successfully"}
    return {"message": "Todo not found"}

# Redirect to Index.html
@app.get("/")
async def redirect_old_path():
    return RedirectResponse(url="/index.html", status_code=302)

# Mount static files
app.mount("/", StaticFiles(directory=get_file("static")), name="static")


def prepare_static_folder():
    localhost = 'http://localhost:8080'
    newApiHost = os.environ['API_HOST']
    folder_path = get_file('static')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                print(f'Reading file: {file_path}')
                file_contents = file.read()
            if localhost in file_contents:
                print(f'localhost found in file: {file_path}')
                file_contents = file_contents.replace(localhost, newApiHost)
            with open(file_path, 'r') as file:
                print(f'localhost replaced to API_HOST in file: {file_path}')
                file.write(file_contents)