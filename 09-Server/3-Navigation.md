# Navigation between pages

At this point we have two HTML pages and a Python script that renders those HTML pages to two different URLs – the home and the about URL.

Now we need to add a menu so that the user can easily navigate through the webpages by just clicking their links. After we have done that the two pages will look like this:

Two web pages we created so far, share the same layout - so we can extract it into a new file and import it into our files.

Let's make a new file, named ```layout.html```:
```html
<!DOCTYPE html>
<html>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">Cool website</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```
First thing, we are using python functions - ```url_for``` in our html. Jinja will look for those functions (anything inside of this ```{{ }}``` ) and evaluate them. In this case, the function is used to create a full link to a given route. So the final html, will be turned into:
```html
<li><a href="http://localhost:5000">Home</a></li>
<li><a href="http://localhost:5000/about">About</a></li>
```

The second part is using ```block``` element, again this is a part of Jinja template and it used to place the content in that place.

We can now change our ```home.html``` and ```about.html``` to use that new layout:
```html
{% extends "layout.html" %}
{% block content %}
  <div class="home">
    <h1>A Python product</h1>
    <p>This website was built with Python via the Flask framework.</p>
  </div>
{% endblock %}
```
This is the ```home.html``` file, as you can see we are using ```extends``` keyword, which as you gave guessed from the name, extend our template from another template.

Next, we are entering the main content of our website inside of ```block``` and since we have given the name of the block in ```template.html``` - content, we should use the same name here.

The final rendered html sent to the user will look like this:
```html
<!DOCTYPE html>
<html>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">Cool website</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="http://localhost:5000">Home</a></li>
            <li><a href="http://localhost:5000/about">About</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>
    <div class="container">
        <div class="home">
            <h1>A Python product</h1>
            <p>This website was built with Python via the Flask framework.</p>
        </div>
    </div>
  </body>
</html>
```
And as you can see the final html, has no python functions or anything else, just the final HTML.

Let's also modify the ```about.html``` page:
```html
{% extends "layout.html" %}
{% block content %}
   <div class="about">
     <h1>About me</h1>
     <p>This is a portfolio site about anything that can be put in a portfolio.</p>
   </div>
 {% endblock %}
```

If we now open the website at localhost:5000, we will see the home page and if we click on the link for about page, we will navigate to the about page.
