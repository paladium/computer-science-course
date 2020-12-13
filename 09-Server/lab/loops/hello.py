#Display a list of shop items
#Each shop item is just a string
#["Laptop", "PC", "Console"]
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    devices = ["PC", "Console", "Laptop", "TV"]
    return render_template('index.html', devices=devices)

#Second page, /items
#List of items
#List of dictionaries
#Load that list from JSON file
# [{"name": "Laptop", "description": "Very perfomant laptop", "price": 1000, "stock": 50}, ...]
#To display those items in a file named items.html
#Each item should be displayed like <li>Name: Laptop, Price: 1000, ...</li>
@app.route('/details')
def details():
    with open("details.json") as file:
        data = json.load(file)
    return render_template('details.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)