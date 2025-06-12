from http.client import HTTPException

from . import con, cur

# conn = get_db_connection()
#     try:
#         with conn.cursor() as cursor:
#             sql = "SELECT username, password FROM users WHERE username = %s"
#             cursor.execute(sql, (username))
#             user = cursor.fetchone()

def find_user(username: str):
    query = f"select * from users where username={username}"
    cur.execute(query)
    result = cur.fetchone()
    if result is None:
        raise HTTPException()
    return result