# Cookies
Cookies are stored on the client’s computer as text files.The aim is to remember and track data that is relevant to customer usage for better visitor experience and website statistics.

The Flask Request object contains the properties of the cookie. It is a dictionary object for all cookie variables and their corresponding values, and the client is transferred.In addition to this, cookies also store the expiration time, path, and domain name of its website.

## Flask cookies

To create a cookie, you need to use the function ```make_response()``` which will construct the final response (html page or string) that will be sent to the user and you can set the cookie on it before returning the final result.

```python

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    username = request.cookie.get("username")
    return "Welcome to dashboard {}".format(username)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.METHOD == 'POST':
        username = request.form["username"]
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie("username", username)
        return resp
    else:
        return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)
```