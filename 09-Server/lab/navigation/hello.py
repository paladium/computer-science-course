from flask import Flask, render_template

#Make a new Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-me')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)