# angular-python-todo

## Alembic Migration Generate
> alembic revision --autogenerate -m "Todo model"

## Update Tables to DB
> alembic upgrade head

## Create binary for linux
pyinstaller main.spec

## Create shell script to set env vars
```
export ALLOWED_ORIGINS=google.com
export APP_ROUTE=/myapp
export DB_USERNAME=<value>
export DB_PASSWORD=<value>
export DB_HOST=<value>
export DB_PORT=3306
export DB_NAME=<value>
```

## Setup
1. Create virtual env
> python -n venv .venv

2. Activate virtual env and install deps
> source .venv/bin/activate
> pip install -r requirements.txt

3. Create Binary
> pyinstaller main.spec

4. Create a shell file (`set_env.sh`) and setup these env vars
```
export ALLOWED_ORIGINS=google.com
export APP_ROUTE=/myapp
export DB_USERNAME=<value>
export DB_PASSWORD=<value>
export DB_HOST=<value>
export DB_PORT=3306
export DB_NAME=<value>
```
Run this file to set env vars
> ./set_env.sh

5. Run binary
> ./dist/main