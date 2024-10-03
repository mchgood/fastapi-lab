from fastapi import FastAPI, APIRouter

user = APIRouter()

@user.get("get")
def get_user():
    return {
        "name":"get user"
    }