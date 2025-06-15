from fastapi import FastAPI, HTTPException, Body, APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from service import login as service

from model.users import LoginUser

router = APIRouter()

# jwt로 로그인 구현
@router.post("/login")
def login_jwt(response: Response, login_user: LoginUser = Body()):
    access_token = service.login_service(login_user)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="strict",
        secure=False,
        path="/"
    )
    response.status_code = status.HTTP_200_OK
    response.body = b"jwt login ok"
    return response

# 로그아웃: 쿠키 없애기
@router.post("/logout")
def logout_jwt(response: Response):
    response.delete_cookie("access_token")
    response.status_code = status.HTTP_200_OK
    response.body = b"jwt logout ok"
    return response

@router.get("/me")
def me(request: Request):
    access_token = request.cookies.get("access_token")
    return service.token_to_user(access_token)