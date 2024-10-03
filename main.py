import uvicorn
from fastapi import FastAPI

from apps.app01 import shop
from apps.app02 import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(shop, prefix="/shop", tags=["shop"])
app.include_router(user, prefix="/user", tags=["user"])

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True, log_level='debug')
