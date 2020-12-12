#Import flask library
from flask import Flask
import my_test
#We are instantiating the class Flask, __name__ - variable provided by python to run our current file
app = Flask(__name__)

#When the user opens the website coolwebserver.com
#I want to serve this function, i want this function to be connected to "/" requests

@app.route('/')
def home():
    return "Hey there!"

@app.route("/about")
def about():
    return "Hello this is the about page"

@app.route("/calculate")
def calculate():
    return str(my_test.calculate(10, 1000))

#Two ways of running
#Changing the port to anothe value
#app.run(debug=True, port=8000)
#We run our application in debug mode
if __name__ == '__main__':
    app.run(debug=True)