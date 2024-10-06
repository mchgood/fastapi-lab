from fastapi import APIRouter

from api.Base import ApiRouter
from views.Base import ViewsAPIRouter

AllRouter = APIRouter()
# api 路由
AllRouter.include_router(ApiRouter)
# 视图路由
AllRouter.include_router(ViewsAPIRouter)