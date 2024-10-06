from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

UserApiRouter = APIRouter(prefix="/user",tags=["user"])

class Login(BaseModel):
    username: str
    password: str
    user: List[int]

@UserApiRouter.post("/login")
def login(data: Login):
    return data