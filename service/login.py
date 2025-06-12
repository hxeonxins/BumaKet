from http.client import HTTPException

from passlib.context import CryptContext
from data import user_repo as fetch_user_by_username
from jose import jwt
from datetime import datetime, timedelta
from data import user_repo as data
from jwt.jwt_util import create_access_token
from model.users import LoginUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def login_service(login_user: LoginUser):
    # db 확인 전달
    f_user = data.find_user(login_user.username)

    # 비밀 번호 확인
    if login_user.password != f_user['password']:
        raise HTTPException()

    # 토큰 생성
    token_data = {
        "username": login_user.username,
        "is_admin": login_user.is_admin,
    }
    access_token = create_access_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}