from fastapi import FastAPI
from controllers import post
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite+aiosqlite:///blog.db"

metadata = sa.MetaData()
engine = create_async_engine(DATABASE_URL)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models import post
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)