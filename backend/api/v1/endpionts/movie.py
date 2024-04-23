from typing import List

from fastapi import APIRouter, Depends

from backend.core import deps
from backend.models import Movie
from backend.schemas import Movie_Pydantic, MovieIn_Pydantic, Response200, Response400

movie = APIRouter(tags=["电影相关"], dependencies=[Depends(deps.get_current_user)])


@movie.get("/movie", summary="电影列表", response_model=List[Movie_Pydantic])
async def movie_list(limit: int = 10, page: int = 1):
    # limit 代表每一页上显示的条数，page代表当前页数，skip代表跳过的条数
    # 比如limit=10,page=2,那么就是从第11条开始显示，即skip=10
    # 换成SQL语句是
    # SELECT * FROM movie LIMIT skip , limit
    # SELECT * FROM movie LIMIT 0 OFFSET 10
    skip = (page - 1) * limit
    # 从数据库中获取所有电影 , await代表异步，使用Movie_Pydantic.from_queryset(Movie.all()]]]]]]]]]])将Tortoise ORM的模型转换为Pydantic模型
    # 主要是为了验证数据的合法性
    return await Movie_Pydantic.from_queryset(Movie.all().offset(skip).limit(limit))


@movie.post("/movie", summary="电影添加")
# 选择使用MovieIn_Pydantic作为请求体，这样可以验证数据的合法性，并且MovieIn_Pydantic中不包含id字段,id is readonly
async def movie_create(movie_form: MovieIn_Pydantic):
    return await MovieIn_Pydantic.from_tortoise_orm(await Movie.create(**movie_form.dict()))


@movie.put("/movie/{pk}", summary="电影编辑")
async def movie_update(pk: int, movie_form: MovieIn_Pydantic):
    if await Movie.filter(pk=pk).update(**movie_form.dict()):
        return Response200()
    return Response400(msg="更新失败")


@movie.delete("/movie/{pk}", summary="电影删除")
async def movie_delete(pk: int):
    if await Movie.filter(pk=pk).delete():
        return Response200()
    return Response400()
