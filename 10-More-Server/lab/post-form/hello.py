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


#Two routes - /login - returns the html page and /doLogin - actually uses the data we send from the form
@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/doLogin', methods=['POST'])
def login():
    #name = request.form["name"]
    #description =....
    username = request.form['username']
    password = request.form["password"]
    age = request.form["age"]
    print(request.form)
    return "Your username is {} and password is {} and age is {}".format(username, password, age)
    #return redirect(url_for('dashboard',name = username))

if __name__ == '__main__':
   app.run(debug = True)
