from tortoise.contrib.pydantic import pydantic_model_creator

from backend.models import Movie

# 生成Pydantic模型
# 主要作用是将Tortoise ORM的模型转换为Pydantic模型
# 在从客户端收到数据的时候，可以使用Pydantic模型进行数据验证
Movie_Pydantic = pydantic_model_creator(Movie, name="Movie")
# exclude_readonly=True表示不包含只读字段，在生成的表中，id是只读的，所以这里不包含id
MovieIn_Pydantic = pydantic_model_creator(Movie, name="MovieIn", exclude_readonly=True)
