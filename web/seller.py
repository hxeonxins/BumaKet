from fastapi import APIRouter, UploadFile,HTTPException
from fastapi.openapi.models import OAuth2
from fastapi.params import Depends, File, Form
from starlette.requests import Request
from typing import List

from jwt.jwt_util import get_current_user
from model.users import UserResponse
from service import product as service

router = APIRouter(prefix="/seller")

@router.post("/products")
def upload_products(
        token: UserResponse = Depends(get_current_user),
        title: str = Form(...),
        description: str = Form(None),
        images: List[UploadFile] = File(...),
):
    try:
        result = service.upload_product(token.user_id, title, description, images)
        return {"message": "상품 업로드가 완료되었습니다.", "image_name": result["image_name"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/products/my")
# def get_my_product(token: Depends(get_current_user)):
#     product_id = ""
#     title = ""
#     like_count = ""
#     return {
#         "product_id": product_id,
#         "title": title,
#         "like_count": like_count
#     }