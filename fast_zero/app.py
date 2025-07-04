from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá Mundo!"}


@app.get("/items")
def read_items():
    return {"items": ["item1", "item2", "item3"]}
