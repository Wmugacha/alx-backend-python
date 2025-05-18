#!/usr/bin/python3
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

def stream_user_ages():
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT age from user_data"
    cursor.execute(query)
    
    for (age,) in cursor:
        yield age

def average_user_ages():
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    average = total / count if count > 0 else 0
    
    print(average)

if __name__ == "__main__":
    average_user_ages()