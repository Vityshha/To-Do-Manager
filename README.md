# DoorsON

## info 

1. FastAPI
2. SQLAlchemy
3. Alembic 
4. pdAdmin 
5. Python 3.11 > x 
6. Для подключения к БД используется ассинхронный движок 

## how start 
1. Запуск сервера - ``uvicorn app.main:app --reload``
2. Скачать pdAdmin и Postgres - ``https://www.postgresql.org/download/``
3. Как обновляем данные в бд, при создании новых сущностей:
- ``alembic init migrations ``
- в alembic.ini меняем путь к папке migrations
- производим махинации в env.py, туда же все инпуты пихаем
4. В корне проекта: 
- ``alembic revision --autogenerate -m 'init'``
- если есть проблемы, то - ``pip install greenlet``
- ну еще в бд стоит проверить нет ли старых данных миграций 
- дальше - ``alembic upgrade head``
