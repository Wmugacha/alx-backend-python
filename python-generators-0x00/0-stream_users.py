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

def stream_users():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT user_id, name, email, age FROM user_data"
    cursor.execute(query)

    for row in cursor:
        yield row

    cursor.close()
    conn.close