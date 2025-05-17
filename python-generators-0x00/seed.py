from contextlib import contextmanager
import mysql.connector
import uuid
import csv

def connect_db():
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user='root',
            password='root',
        )
        print("Connected Successfully!!")
        return conn


def create_database(connection):
    cursor = connection.cursor()

    query = "CREATE DATABASE IF NOT EXISTS ALX_prodev"

    cursor.execute(query)
    connection.commit()
    cursor.close()

def connect_to_prodev():
        conn = connect_db()
        cursor = conn.cursor()

        query = "USE ALX_prodev"
        cursor.execute(query)
        print("Switched to ALX_prodev database.")
        cursor.close()
        return conn

def create_table(connection):
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS user_data (
    user_id CHAR(36) Primary Key,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL NOT NULL,
    INDEX (user_id)
    )
    """

    cursor.execute(query)
    connection.commit()
    print("Tables Created on ALX_prodev.")
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()

    with open(data, newline='') as userdata:
        reader = csv.DictReader(userdata)
        for row in reader:
            user_id = str(uuid.uuid4())
            query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (user_id, row["name"], row["email"], row["age"]))

    connection.commit()
    cursor.close()
    print("User data added sucessfully")

conn = connect_db()
create_database(conn)

conn = connect_db()
cursor = conn.cursor()
cursor.execute("USE ALX_prodev")
cursor.close()
create_table(conn)

conn = connect_db()
cursor = conn.cursor()
cursor.execute("USE ALX_prodev")
cursor.close()
insert_data(conn, "user_data.csv")