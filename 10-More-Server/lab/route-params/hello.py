from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open("details.json") as file:
        data = json.load(file)
    return render_template('index.html', data=data)

#Add a new route, named get_time with parameter <name>
#Find an item in a list of items using name
#Return the template named item.html with the found item
@app.route('/product/<name>')
def get_item(name):
    with open("details.json") as file:
        data = json.load(file)
    s = {}
    for i in data:
        if name == i['name']:
            s = i
    return render_template('item.html', item=s)

@app.route("/user/<name>/<repository>")
def test_route(name, repository):
    return "{} your repo is {}".format(name, repository)


def my_url_for(func_name, name="", repository=""):
    return "{}/{}/{}".format(func_name, name, repository)

print(my_url_for("get_user", "javid", "WebShop"))
print(my_url_for("get_user", name="javid", repository="WebShop"))

if __name__ == '__main__':
    app.run(debug=True)