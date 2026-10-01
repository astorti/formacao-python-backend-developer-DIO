from fastapi import FastAPI
from datetime import UTC, datetime

app = FastAPI()

posts_db = [
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), "published": False}
]


@app.get("/posts/")
def read_posts(published: bool, limit: int, skip: int = 0):
    return [post for post in posts_db[skip: skip + limit] if post["published"] is published]
