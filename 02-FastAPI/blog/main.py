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

tags_metadata = [
    {
        "name": "post",
        "description": "Operações para manter posts.",
    },
]

servers = [
    {"url": "http://localhost:8000", "description": "Ambiente de desenvolvimento"},
]

app = FastAPI(
    lifespan=lifespan,
    title="Blog API com FastAPI",
    version="1.2.0",
    summary="API para blog pessoal.",
    description="""
O blog API ajuda você a criar seu blog pessoal. 🚀

### Posts

Você será capaz de fazer:

* **Criar posts**.
* **Recuperar posts**.
* **Recuperar posts por ID**.
* **Atualizar posts**.
* **Excluir posts**.
                """,
    openapi_tags=tags_metadata,
    servers=servers,
    redoc_url=None, 
    # openapi_url=None,
)

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