from typing import Optional
from fastapi import FastAPI, Header
from fastapi import FastAPI, Response, status
import json

app = FastAPI()


@app.get("/auth")
async def root(response: Response, authorization: Optional[str] = Header(None)):
    # check authorization
    if authorization is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return
    response.headers["X-User-Data"] = json.dumps({"username": "root", "role": "admin"})
    return
