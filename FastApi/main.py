from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:  # http://127.0.0.1:8000/items/10?q=100
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")  # e.g.: /home/johndoe/myfile.txt
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
