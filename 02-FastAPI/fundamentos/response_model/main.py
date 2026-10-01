from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str

@app.get('/books', response_model=Book)
def books():
    return {'title': 'As Aventuras de Sherlock Holmes', 'author': 'Arthur Conan Doyle'}