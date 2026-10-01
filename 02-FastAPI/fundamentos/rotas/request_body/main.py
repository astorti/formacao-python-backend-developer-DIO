from pydantic import BaseModel
from fastapi import FastAPI, status
from datetime import UTC, datetime

app = FastAPI()

class Post(BaseModel):
    title:str
    date: datetime = datetime.now(UTC)
    published: bool = False

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    return post
