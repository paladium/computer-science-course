# Route parameters
You could add parameters to your routes which will act as variables.

Take for example the following route:
```html
https://myshop.com/item/23456
```
In this case, the main route (function) will be item and the route param will be 23456, which is the id of the item we want to view.

## Flask Routes
To add a new route param:
```python
@app.route('/product/<id>')
def get_item(id):
  return "The product is " + str(id)
```
You could also provide multiple route params (however it is not advisable to have more than 3 route params and instead use post form):
```python
@app.route('/user/<username>/<repository>')
def get_repository(username,repository):
  return "{} has {} repository".format(username, repository)
```