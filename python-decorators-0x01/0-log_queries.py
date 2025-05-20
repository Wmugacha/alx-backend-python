import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

 """ YOUR CODE GOES HERE"""
def log_queries():
    time_log = date.datetime.now()
    query_log = conn.set_trace_callback(print)
    print(f"{time_log} : {query_log}")


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