from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return json.dumps([
        {
            "name": "ilkin",
            "age": 22
        },
        {
            "name": "Javid",
            "age": 16
        }
    ])

if __name__ == '__main__':
    app.run(debug=True)
