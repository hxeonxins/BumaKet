from cache import redis_client

def get_like_score(product_id: int):
    score = redis_client.zscore("like_ranking", product_id)
    return int(score) if score else 0

def toggle_like(product_id: int, device_hash: str):
    product_key = f"like:{product_id}"
    user_key = f"user_likes:{device_hash}"

    if redis_client.sismember(product_key, device_hash):
        #좋아요 취소
        redis_client.srem(product_key, device_hash)
        redis_client.srem(user_key, product_id)
        redis_client.zincrby("like_ranking", -1, product_id)
    else:
        #좋아요 증가
        redis_client.sadd(product_key, device_hash)
        redis_client.sadd(user_key, product_id)
        redis_client.zincrby("like_ranking", 1, product_id)
