from typing import Any

from fastapi import APIRouter, Depends

from backend.core import deps
from backend.models import User
from backend.schemas import User_Pydantic, UserIn_Pydantic, Response200, Response400

user = APIRouter(tags=["用户相关"], dependencies=[Depends(deps.get_current_user)])


@user.get("/user", summary="当前用户")
async def user_info(user_obj: Any = Depends(deps.get_current_user)):
    """
    获取当前用户信息
    username : str 必传
    password : str 必传
    :param user_obj: 得到的当前用户对象
    :return: 返回当前用户对象
    """
    return await User_Pydantic.from_tortoise_orm(user_obj)


@user.put("/user", summary="修改个人信息")
async def user_update(user_form: UserIn_Pydantic, user_obj: User = Depends(deps.get_current_user)):
    """
    修改当前用户对象
    username : str 必传
    password : str 必传
    :param user_form:
    :return:
    """
    user_form.username = user_obj.username
    user_form.password = user_obj.password
    if await User.filter(username=user_obj.username).update(**user_form.dict()):
        return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))
    return Response400(msg="更新失败")
