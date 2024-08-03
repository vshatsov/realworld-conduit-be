from typing import Union

from fastapi import FastAPI

from conduit.settings import SETTINGS

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "PORT": SETTINGS.PORT}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def main():
    import uvicorn
    uvicorn.run(app, port=SETTINGS.PORT)


if __name__ == "__main__":
    main()