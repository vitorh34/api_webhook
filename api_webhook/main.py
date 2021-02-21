from typing import Optional
from fastapi import FastAPI, Request, Header
from pydantic import BaseModel
import json
import base64
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Item(BaseModel):
    username: str
    clientid: str
    mountpoint: str
    qos: str
    topic: str
    payload: str
    retain: bool

    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None

    # {
    #     "username": "username",
    #     "client_id": "clientid",
    #     "mountpoint": "",
    #     "qos": 1,
    #     "topic": "a/b",
    #     "payload": "hello",
    #     "retain": false
    # }

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/item/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}

@app.post("/mqttbroker/on_publish")
async def print_content(request: Request):
    da = await request.form()
    da = jsonable_encoder(da)
    print(da)

    # print(item)
    # print()
    # print(request.base_url)
    # print()
    # print(request.headers['content-type'])
    # print()
    # body = b''
    # async for chunk in request.stream():
    #     body += chunk
    #     print(body)
    # print()
    # # print(dir(request))
    return json.dumps({'result': 'ok'})