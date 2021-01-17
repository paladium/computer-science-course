from db.database import Database
from db.course import CourseManager
import os
from flask import Flask
import json

#Two things:
#Import os
#Read env variables and pass them to db object
host = os.environ.get("MYSQL_HOST")
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
database = os.environ.get("MYSQL_DATABASE")

DB = Database(host, user, password, database)
COURSE_MANAGER = CourseManager(DB)

#Create a new flask app
APP = Flask(__name__)

@APP.route("/courses")
def list_courses():
    courses = COURSE_MANAGER.list_all()
    return json.dumps(courses)

#Bootstrap function connects to database and starts our server
def bootstrap():
    print("Connecting to database")
    DB.connect()
    print("Connected to database")

    print("Start migration")
    DB.migrate('sql/migration.sql')
    print("Finished migration")

    #Run flask app, without checking for __main__
    APP.run(debug=True)