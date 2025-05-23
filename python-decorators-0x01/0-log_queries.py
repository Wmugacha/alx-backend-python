import sqlite3
import functools
from datetime import datetime

#Decorator to lof SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        def logger(statement):
            print(f"{datetime.now()} : Executing SQL: {Statement}")

        conn = sqlite3.connect("users.db")
        conn.set.trace_callback(logger)
        
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")