from fastapi import FastAPI, Request
from controllers import post
from fastapi.responses import JSONResponse
from exceptions import NotFoundPostError


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