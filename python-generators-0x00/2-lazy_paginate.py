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

def lazy_paginate(page_size):
    conn = connect_db()
    cursor = conn.cursor()
    offset = 0

    def paginate_users(page_size, offset):
        query = "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        return cursor.fetchall()

    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
    
    cursor.close()
    conn.close()