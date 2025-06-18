import hashlib
import os
import shutil

from fastapi import APIRouter, UploadFile,HTTPException
from fastapi.params import Depends, File, Form
from starlette.requests import Request

from service import product as service

router = APIRouter(prefix="/product")

def generate_device_id(request: Request ) -> str:
    ip = request.client.host
    user_agent = request.headers.get("user-agent", "unknown")
    device_id = f"{ip}${user_agent}"
    return hashlib.sha256(device_id.encode()).hexdigest()

@router.post("/{product_id}/like")
def get_product_like(product_id: int,
                     device_hash=Depends(generate_device_id)):
    return service.toggle_like(product_id, device_hash)

@router.post("/products")
def upload_products(
        title: str = Form(...),
        description: str = Form(None),
        image: UploadFile = File(...),
):
    try:
        result = service.upload_product(title, description, image)
        return {"message": "상품 업로드가 완료되었습니다.", "filename": result["image_name"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
