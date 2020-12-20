from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, make_response

app = Flask(__name__)

#Two templates
#First is the home page named index.html with the link to /login route
#Second page is the login.html with username and password inputs. The form is posted /login route.

#First part, we simply render a home page
@app.route('/')
def index():
   return render_template('index.html')


#Secure page, we use the cookies object to get the cookie by name
@app.route('/dashboard')
def dashboard():
    if request.cookies.get("username") is None:
        return "Forbidden"
    username = request.cookies.get("username")
    return "Welcome to dashboard {}".format(username)


@app.route('/doLogin', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "test" and password == "test":
        #Request - is what you send from the user, response is what you get from the server
        #make_response to make our final response, in this case redirect to dashboard
        #We set our cookie on that response and we return the response
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie("username", username)
        return resp
    else:
        return "Access denied"

@app.route('/login')
def login_page():
    return render_template('login.html')



if __name__ == '__main__':
   app.run(debug = True)