import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user='root',
        password='root',
        database="ALX_prodev"
    )
    print("Connected Successfully!!")
    return conn

def paginate_users(page_size, offset):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    return cursor.fetchall()

    cursor.close()
    conn.close()

def lazy_paginate(page_size):
    offset = 0

    while True:
        page = paginate_users(page_size, offset)
        yield page
        offset += page_size