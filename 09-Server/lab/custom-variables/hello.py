from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Javid'
    age = 16
    return render_template('index.html', title='Welcome', username=name, userage=age)

if __name__ == '__main__':
    app.run(debug=True)