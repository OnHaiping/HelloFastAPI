from tortoise.contrib.pydantic import pydantic_model_creator

from backend.models import User

User_Pydantic = pydantic_model_creator(User, name="User", exclude=tuple(['password']))
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn")
