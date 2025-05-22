import mysql.connector

class ExecuteQuery:
    def __init__(self, host, user, password, database, query, params=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.cursor = self.connection.cursor()
            if self.params:
                self.cursor.execute(self.query, self.params)
            else:
                self.cursor.execute(self.query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise err

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.connection:
            if exc_type is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()

query = "SELECT * FROM users WHERE age > %s"
params = (25,)

with ExecuteQuery("localhost", "root", "root", "ALX_prodev", query, params) as results:
    for row in results:
        print(row)