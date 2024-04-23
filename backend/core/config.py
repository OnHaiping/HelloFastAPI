"""
这个文件配置一些不会变的信息
例如SECRET_KEY、SECRET_KEY、ACCESS_TOKEN_EXPIRE_MINUTES
"""
import secrets
from typing import Optional

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """
    配置类
    """
    # 描述信息
    TITLE: Optional[str] = "电影列表接口"

    DESC: Optional[str] = """
    - 电影列表项目，基于HelloFlask开发的实战项目
    - 实现：FastAPI + Tortoise ORM + Pydantic + MySQL
    """

    # # 数据库连接信息
    # MYSQL_USER: str
    # MYSQL_PASSWORD: str
    # MYSQL_HOST: str
    # MYSQL_PORT: str
    # MYSQL_DB: str

    # token配置
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # token过期时间,单位是分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
