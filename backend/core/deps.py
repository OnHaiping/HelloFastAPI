from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from backend.core import settings
from backend.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    oauth2_scheme --> 从请求头中取到 Authentication: Bearer token
    解析token，获取当前用户对象
    :param token: 登录之后获取到的token
    :return: 当前用户对象
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub", None)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await User.get(username=username)
    if user is None:
        raise credentials_exception
    return user
