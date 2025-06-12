import pymysql
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        password="1234",
        db="buma_dev",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
con = get_db_connection()
cur = con.cursor()