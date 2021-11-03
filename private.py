from typing import Optional
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/private")
async def root(x_user_data: Optional[str] = Header(None)):
    return {"message": "Hello World", "user": x_user_data}
