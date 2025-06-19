from typing import Optional

from data import get_db_connection

def insert_product(user_id: int, title: str, description: Optional[str], image_url: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO products (user_id, title, description, image_url) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (user_id, title, description, image_url))
        conn.commit()
        return cursor.lastrowid  # 생성된 product_id 반환
    finally:
        cursor.close()
        conn.close()

def insert_product_image(product_id: int, image_url: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO product_images (product_id, image_url) VALUES (%s, %s)"
        cursor.execute(sql, (product_id, image_url))
        conn.commit()
    finally:
        cursor.close()
        conn.close()