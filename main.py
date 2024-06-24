import uvicorn
from dotenv import load_dotenv
load_dotenv()
from app.main import app, get_file, prepare_static_folder
import sys
import os
from alembic import command
from alembic.config import Config

def get_db_url():
    DB_USER=os.getenv('DB_USERNAME')
    DB_PASS=os.getenv('DB_PASSWORD')
    DB_HOST=os.getenv('DB_HOST')
    DB_PORT=os.getenv('DB_PORT')
    DB_NAME=os.getenv('DB_NAME')
    url = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(url)
    return url

if __name__ == "__main__":
    alembic_cfg = Config(get_file('alembic.ini'))
    alembic_cfg.set_main_option('script_location', get_file('alembic'))
    alembic_cfg.set_main_option('sqlalchemy.url', get_db_url())
    command.upgrade(alembic_cfg, 'head')

    # Read all files in static folder, rename host url
    prepare_static_folder()

    # Start server
    uvicorn.run(app, host="0.0.0.0", port=8080)
    