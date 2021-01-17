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

#Filter
mycursor.execute("SELECT * FROM customers ORDER BY name")

#Obtain the result from filter
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Select only name from customers
mycursor.execute("SELECT name FROM customers")

#Obtain the result from filter
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Cursor is closed automatically