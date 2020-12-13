# Post route with Form
Flask supports HTTP POST requests (posting an HTML form). Let's first create a new html file:
```html
<html>
   <body>
      <form action = "{{ url_for('login') }}" method = "post">
         <p>Username:</p>
         <p><input type = "text" name="username"/></p>
         <p><input type="submit" value="submit" /></p>
      </form>
   </body>
</html>
```
Next create the hello.py document:
```python
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
   return 'Welcome to my website'

@app.route('/dashboard/<name>')
def dashboard(name):
    return "Welcome to dashboard {}".format(name)

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      username = request.form['username']
      return redirect(url_for('dashboard',name = user))
   else:
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)
```