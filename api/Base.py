# -*- coding:utf-8 -*-
"""
@Des: 基本路由
"""
from fastapi import APIRouter

from api.User import UserApiRouter

ApiRouter = APIRouter(prefix="/api")

ApiRouter.include_router(UserApiRouter)

@ApiRouter.get('/')
async def home(num: int):
    return {
        "num": num
    }
