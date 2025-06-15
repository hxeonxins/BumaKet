# User 모델 생성
from datetime import datetime

from pydantic import BaseModel

class LoginUser(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class UserResponse(BaseModel):
    user_id: int
    username: str