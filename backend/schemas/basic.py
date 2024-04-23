"""
这个文件定义了一些基础的响应模型
"""
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """
    业务状态码
    """
    SUCCESS = 200
    FAIL = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500


class ResponseBasic(BaseModel):
    """
    响应模型
    """
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="业务状态码，200成功，400失败")
    data: Any = Field(default=None, description="数据结果")
    msg: str = Field(default="请求成功", description="提示")


class Response200(ResponseBasic):
    code: CodeEnum = CodeEnum.SUCCESS
    msg: str = "请求成功"


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = "请求失败"


class ResponseToken(Response200):
    access_token: str
    token_type: str = Field(default="bearer", description="token类型")
