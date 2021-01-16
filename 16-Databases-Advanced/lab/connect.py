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

print(mydb)

#List tables
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#Create a table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")