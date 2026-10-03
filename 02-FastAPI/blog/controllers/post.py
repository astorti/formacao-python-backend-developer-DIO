from fastapi import status, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostIn):
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int = 0):
    return []
