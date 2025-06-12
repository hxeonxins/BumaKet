from datetime import datetime

from pydantic import BaseModel

class Like(BaseModel):
    like_id: int
    product_id: int
    device_hash: str
    liked_at: datetime