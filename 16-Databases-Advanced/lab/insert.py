import os
import mysql.connector

#Make sure that we do not expose our credentials & we can change between environments
host = os.environ.get("MYSQL_HOST")
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
database = os.environ.get("MYSQL_DATABASE")

mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database=database,
)

#Insert data
#We get the cursor to work with database
mycursor = mydb.cursor()

#Run in loop - five times
n=0
while n != 6:
    #We make the sql query string
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

    #Tuple of values to insert
    val = ("John", "Highway 21")

    #1 step - insert new data

    #Execute the statement with provided values. Those values will be sanitized - stripped of dangerous statements.
    mycursor.execute(sql, val)
    #Number of steps, commit saves - ctrl+s to the database
    mydb.commit()
    n += 1
    print(mycursor.rowcount, "record inserted.")