from fastapi import FastAPI, APIRouter

shop = APIRouter()

@shop.get("/get")
def get_shop():
    return {
        "name":"get shop"
    }