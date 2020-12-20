from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

#Add a new route, named error
#If the username is not admin, redirect the user to that route
#error route should return a template named error.html, which displays a red text with the error Forbidden
#Instead of the same error text in html, i want you to pass the error as a variable to template and use it inside of the template
@app.route('/error')
def error():
    text = 'Access denied'
    return render_template('error.html', text=text)

#Purpose: render the login template to ask the user for his username
@app.route('/')
def index():
    #New template with html form, one field - name: username, submit button to login route
    return render_template('login.html')

#Purpose: to check if we provided correct username
@app.route('/login',methods = ['POST']) 
def login(): 
    #Save the posted username to a variable
    username = request.form["username"]
    #Check if the username is admin
    if username == "admin":
        #Two parts - url you want to redirect to, url_for('success') = /success
        #Second part - redirect takes the string and goes to that url
        success_route = url_for('success')
        return redirect(success_route)
    else:
        error = url_for('error')
        return redirect(error)

#Purpose: success page to be seen after successfull login
@app.route('/success')
def success():
    return 'logged in successfully'
	
if __name__ == '__main__':
   app.run(debug = True)