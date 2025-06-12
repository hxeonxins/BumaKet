from datetime import datetime

from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    user_id: str
    title: str
    description: str
    image_url: str
    created_at: datetime

class ProductImage(BaseModel):
    image_id: int
    product_id: int
    image_url: str