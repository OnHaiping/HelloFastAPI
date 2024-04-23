"""
登录、注册
"""

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from backend.models import User
from backend.core import verify_password, create_access_token
from backend.schemas import UserIn_Pydantic, Response200, Response400, ResponseToken, User_Pydantic

login = APIRouter(tags=["认证相关"])


@login.post("/login", summary="登录")
async def user_login(from_data: OAuth2PasswordRequestForm = Depends()):
    # 异步获取账号信息，然后进行验证
    user = await User.get_or_none(username=from_data.username)
    if user is None:
        return {"msg": "账号不存在，请注册"}
    if verify_password(from_data.password, user.password):
        token = create_access_token({"sub": user.username})
        return ResponseToken(data={"token": f"bearer {token}"}, access_token=token)
    return Response400(msg="请求失败")


@login.post("/user", summary="新增用户")
async def user_create(user: UserIn_Pydantic):
    await User.create(**user.dict())
    return Response200(data = await User_Pydantic.from_queryset_single(await User.create(**user.dict())))
