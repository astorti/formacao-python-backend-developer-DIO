from fastapi import FastAPI
from controllers import post
from contextlib import asynccontextmanager
from database import metadata, engine

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