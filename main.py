import uvicorn
from app.main import app
import sys
import os
from alembic import command
from alembic.config import Config

def get_app_global_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(__file__)

def get_db_url():
    DB_USER=os.getenv('DB_USERNAME')
    DB_PASS=os.getenv('DB_PASSWORD')
    DB_HOST=os.getenv('DB_HOST')
    DB_PORT=os.getenv('DB_PORT')
    DB_NAME=os.getenv('DB_NAME')
    return  f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_file(file):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, file)
    return os.path.join(os.path.dirname(__file__), file)


if __name__ == "__main__":
    alembic_cfg = Config(get_file('data/alembic.ini'))
    alembic_cfg.set_main_option('script_location', get_file('data/alembic'))
    alembic_cfg.set_main_option('sqlalchemy.url', get_db_url())
    command.upgrade(alembic_cfg, 'head')
    uvicorn.run(app, host="0.0.0.0", port=8080)
    