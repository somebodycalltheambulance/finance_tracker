from fastapi import FastAPI
from app.api import transactions
from app.core.init_db import init_db

async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(transactions.router)