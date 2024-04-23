from fastapi import APIRouter
from .endpionts import *

v1 = APIRouter(prefix="/v1")

v1.include_router(login)
v1.include_router(movie)
v1.include_router(user)
