from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from core.Response import success, fail
from models.UserPo import UserPo

UserApiRouter = APIRouter(prefix="/user", tags=["user"])


class UserDto(BaseModel):
    username: str
    password: str


@UserApiRouter.post("/login", summary="登录")
def login(data: UserDto):
    db_user = UserPo().get_or_none(username=data.username)
    if not db_user:
        return fail(msg="用户不存在")
    if db_user.password != data.password:
        return fail(msg="密码错误")
    return success(msg="登录成功")


@UserApiRouter.post("/register", summary="注册")
def login(data: UserDto):
    add_user = UserPo().create(username=data.username, password=data.password)
    return success(data=add_user.__dict__)
