from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message
app = FastAPI(title="Estudo sobre FastAPI", description="A simple FastAPI application", version="1.0.0")


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}

