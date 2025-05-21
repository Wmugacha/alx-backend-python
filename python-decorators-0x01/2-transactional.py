import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        class DatabaseTransaction:
            def __init__(self, connection):
                self.connection = connection
            
            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_value, exc_traceback):
                if exc_type:
                    print(f"An exception of type {exc_type} occurred: {exc_value}")
                    self.connection.rollback()
                else:
                    self.connection.commit()

        conn = args[0]
        with DatabaseTransaction(conn):
            return func(*args, **kwargs)
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 

#Update user's email with automatic transaction handling 
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')