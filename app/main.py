from fastapi import FastAPI
from app.api import transactions
from app.core.init_db import init_db
from app.api.transactions import router as transaction_router

async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
