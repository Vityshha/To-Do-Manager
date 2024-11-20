from fastapi import FastAPI


from app.workers.router import router as router_workers
from app.users.router import router as router_register
from app.users.router import router as router_users
from app.reviews.router import router as router_reviews
from app.orders.router import router as router_orders
from app.descriptions.router import router as router_descriptions
from app.deadlines.router import router as router_deadlines

app = FastAPI()


app.include_router(router_workers)
app.include_router(router_register)
app.include_router(router_users)
app.include_router(router_reviews)
app.include_router(router_orders)
app.include_router(router_descriptions)
app.include_router(router_deadlines)


