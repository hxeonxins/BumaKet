from typing import Optional, List
import os, shutil, datetime
from fastapi import UploadFile, HTTPException
from data.product_repo import insert_product, insert_product_image
import cache.like as like_cache

def toggle_like(product_id: int, device_hash: str):
    like_cache.toggle_like(product_id, device_hash)
    score = like_cache.get_like_score(product_id)

    return {
        "product_id": product_id,
        "like_count": score
    }

def upload_product(title: str, description: Optional[str], images: List[UploadFile]):
    product_id = None
    save_name = None
    dummy_user_id = 1  # 임시 유저 ID
    for idx, image in enumerate(images):
        # 0. 이미지 타입 검사
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="이미지 파일만 업로드 가능합니다")

        # 1. 이미지 저장
        name, ext = os.path.splitext(image.filename)
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        save_name = f"{name}_{timestamp}{ext}"
        image_path = os.path.join("./uploads", save_name)

        # 업로드 폴더 없으면 생성
        os.makedirs("./uploads", exist_ok=True)

        image.file.seek(0)  # 파일 포인터 초기화
        with open(image_path, "wb") as f:
            shutil.copyfileobj(image.file, f)

        image_url = f"/uploads/{save_name}"  # 실제로 DB에 저장할 경로

        #if 첫 번째 이미지인가, return으로 p id 받아와야함, products에 저장
        if idx == 0:
            # 2. 제품 DB 저장
            product_id = insert_product(dummy_user_id, title, description, image_url)
            # return {"product_id": insert_product(dummy_user_id, title, description, image.filename)}
        #else pid와 이미지를 product_image테이블에 저장
        else:
            insert_product_image(product_id, image_url)
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="이미지 파일만 업로드 가능")

    return {"product_id": product_id, "image_name": save_name}
