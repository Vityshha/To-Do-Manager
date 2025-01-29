from fastapi import FastAPI
import uvicorn

from app.users.router import router as router_register
from app.users.router import router as router_users
from app.columns.router import router as router_columns
from app.board_members.router import router as router_board_members
from app.tasks.router import router as router_tasks
from app.boards.router import router as router_boards

app = FastAPI(title='To-Do-Manager')


app.include_router(router_register)
app.include_router(router_users)
app.include_router(router_columns)
app.include_router(router_board_members)
app.include_router(router_tasks)
app.include_router(router_boards)



if __name__ == '__main__':
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


