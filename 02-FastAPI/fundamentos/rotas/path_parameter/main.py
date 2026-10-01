from fastapi import FastAPI
from datetime import UTC, datetime
app = FastAPI()


@app.get("/posts/{framework}")
def read_posts(framework):
# def read_posts(framework: str): # Path Paramenter with types
    return {
        "posts": [
            {"title": f"Conhecendo o framework {framework}", "date": datetime.now(UTC)},
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)}
        ]
    }
