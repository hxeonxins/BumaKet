from fastapi import APIRouter, UploadFile,HTTPException
from fastapi.params import Depends, File, Form
from starlette.requests import Request
from typing import List

from service import product as service

router = APIRouter(prefix="/seller")

@router.post("/products")
def upload_products(
        title: str = Form(...),
        description: str = Form(None),
        images: List[UploadFile] = File(...),
):
    try:
        result = service.upload_product(title, description, images)
        return {"message": "상품 업로드가 완료되었습니다.", "image_name": result["image_name"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/products/my")
# def get_my_product(token: Depends(get_current_user)):
