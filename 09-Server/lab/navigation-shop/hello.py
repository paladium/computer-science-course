#Flask app with two routes - home and add-item
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-item')
def add_item():
    return render_template('add-item.html')

if __name__ == '__main__':
    app.run(debug=True)