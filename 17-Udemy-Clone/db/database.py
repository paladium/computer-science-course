import mysql.connector

class Database:
    #Write init method to accept four parameters - host, username, password & db name
    def __init__(self, host, username, password, db_name):
        self.host = host
        self.username = username
        self.password = password
        self.db_name = db_name
    #Write a method called connect which connects to database & saves the db object in class
    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.db_name,
        )
    #Write a method get_cursor
    def get_cursor(self):
        return self.mydb.cursor(dictionary=True)

    #Migrate method, filename and it runs the migration
    def migrate(self, filename):
        cursor = self.get_cursor()
        with open(filename) as f:
            cursor.execute(f.read(), multi=True)