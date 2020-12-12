# Passing variables to HTML template
We can now see how to pass custom variables inside of HTML templates.

Let's make a new project with the file named ```index.html```:
```html
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>Hello {{ username }}</h1>
    </body>
</html>
```

As make a new file: ```hello.py```:
```python
from flask import render_template
@app.route('/')
def index():
    name = 'Ilkin'
    return render_template('index.html', title='Welcome', username=name)
```
If we now launch the server and visit: ```localhost:5000```, we will see the title of our page to be equal to ```Welcome``` and the h1 tag: ```Hello Ilkin```.

## If statements
We can use conditional statements in our html templates:
```html
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        {% if username == "Robot": %}
            <h1>Hello Robot, are you alive?</h1>
	    {% else %}
            <h1>Hello {{ username }}</h1>
	    {% endif %}
    </body>
</html>
```

## For loops
We can display a list of items in a loop:
```html
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <ul>
        {% for member in members: %}
            <li>{{ member }}</li>
	    {% endfor %}
	</ul>
    </body>
</html>
```
And provide the variable as usual in our route:
```python
@app.route('/')
def index():
    users = [ 'Ilkin','Javid','Bot' ]
    return render_template('index.html', title='Welcome', members=users)
```