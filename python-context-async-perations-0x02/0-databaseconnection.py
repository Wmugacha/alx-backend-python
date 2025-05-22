import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            return self.connection
        except mysql.connector.Error as err:
            raise err

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()

with DatabaseConnection("localhost", "root", "root", "ALX_prodev") as conn:
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)