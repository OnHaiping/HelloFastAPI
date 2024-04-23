from tortoise.contrib.pydantic import pydantic_model_creator

from backend.models import User

User_Pydantic = pydantic_model_creator(User, name="User", exclude=tuple(['password']))
# 去掉id字段，因为id是只读的
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
