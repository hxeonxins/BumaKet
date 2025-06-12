import cache.like as like_cache

def toggle_like(product_id: int, device_hash: str):
    like_cache.toggle_like(product_id, device_hash)
    score = like_cache.get_like_score(product_id)

    return {
        "product_id": product_id,
        "like_count": score
    }