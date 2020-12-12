from flask import Flask, render_template

#Make a new Flask app
app = Flask(__name__)

#Make a new route, bind every request that comes to / to our function home()
#Our function home, then render_template, will look for home.html inside of templates/ folder
#Finally it will open that file, convert to string
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add-item")
def add_item():
    return render_template("add-item.html")

if __name__ == '__main__':
    #Running on port 80
    #app.run(debug=True, port=80)
    app.run(debug=True)