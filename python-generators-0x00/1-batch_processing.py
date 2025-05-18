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

def stream_users_in_batches(batch_size):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT user_id, name, email, age FROM user_data"
    cursor.execute(query)

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_batch = [row for row in batch if row[3] > 25]
        for row in filtered_batch:
            yield row