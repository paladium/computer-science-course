# Introduction to Flask

First let's install flask:
```bash
pip install flask
```

Then create the following file:
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hey there!"
if __name__ == '__main__':
    app.run(debug=True)
```

And run the file, open the browser at localhost:5000 to view your first website.

## Routes

Clients send requests to the webserver, in turn, sends them to the Flask application instance.

The instance needs to know what code needs to run for each URL requested, keeps a mapping of URLs to Python functions.

The association between a URL and the function that handles it is called a route, most convenient way to define a route in a Flask application is through the (app.route).

Decorator exposed by the application instance, which registers the 'decorated function,' decorators are python feature that modifies the behavior of a function:
```python
@app.route('/')
def home():
    return "Hey there!"
```
We are creating the route "/", which means if the user opens the browser at location: localhost:5000 (without slash) it will execute our function.


Server Startup – The application instance has a ‘run’ method that launches flask’s integrated development web server:
```python
if __name__ == '__main__':
    app.run(debug=True)
```
Once the script starts, it waits for requests and services in a loop.

We have a running website with some content returned  by the Python function. As you can imagine, returning plain strings from a function doesn't take us anywhere far.

If you want to make something more serious and more visually appealing, you would want to incorporate HTML files along your Python file and have your Python code return HTML pages instead of plain strings.



