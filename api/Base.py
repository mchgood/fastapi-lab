# -*- coding:utf-8 -*-
"""
@Des: 基本路由
"""
from fastapi import APIRouter
router = APIRouter()

@router.get('/')
async def home(num: int):
    return {
        "num": num
    }
