from fastapi import status, APIRouter
from datetime import UTC, datetime
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

posts_db = [
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), "published": False}
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostIn):
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int = 0):
    tail = skip + limit
    return [post for post in posts_db[skip: tail] if post["published"] is published]

@router.get("/{framework}", response_model=PostOut)
def read_posts(framework: str):
    return {
        "posts": [
            {"title": f"Conhecendo o framework {framework}", "date": datetime.now(UTC)},
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)}
        ]
    }
