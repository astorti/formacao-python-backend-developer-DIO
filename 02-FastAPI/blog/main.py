from fastapi import FastAPI, Request
from controllers import post
from contextlib import asynccontextmanager
from database import metadata, engine
from fastapi.responses import JSONResponse
from exceptions import NotFoundPostError

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

@app.exception_handler(NotFoundPostError)
async def not_found_post_exception_handler(
    request: Request, 
    exc: NotFoundPostError
):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )