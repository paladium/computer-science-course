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

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Park Lane 38")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")