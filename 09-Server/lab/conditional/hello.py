from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Trump'
    #Country - AZ, USA
    #If we pass AZ language, we should greet our user in azeri
    #If USA, we greet in English
    country = 'RU'
    return render_template('index.html', title='Welcome', username=name, lang=country)

if __name__ == '__main__':
    app.run(debug=True)