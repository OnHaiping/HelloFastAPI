"""
create app
"""
import logging
import os
import sys

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .v1 import v1

app = FastAPI()

app.include_router(v1, prefix="/api")

# 下面这部分是logging，用于控制tortoise的日志记录行为
fmt = logging.Formatter(
    fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)
sh.setFormatter(fmt)

# will print debug sql
logger_db_client = logging.getLogger("tortoise.db_client")
logger_db_client.setLevel(logging.DEBUG)
logger_db_client.addHandler(sh)

logger_tortoise = logging.getLogger("tortoise")
logger_tortoise.setLevel(logging.DEBUG)
logger_tortoise.addHandler(sh)

# 连接mysql数据库的URL
DATABASE_URL = "mysql://root:15066577233@localhost:3306/test1"

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["backend.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
