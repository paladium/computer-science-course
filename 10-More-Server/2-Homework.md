# Homework - Extended Online shop
Your online shop from previous homework should now be extended with more features and Flask web server.

It should have 3 pages:
- Main page with all the items
- Individual page for each item
- Add item page

## Main page
Main page will contain a list of items. Items will be stored in a json file named ```items.json```. This file will be loaded and the data will be sent to the html to render. HTML should render a list of items using ```for``` loop.

## Individual Item
The page for individual item should contain the name, description and the link to the image (link on the internet not local). The id the item to show should be taken from the route parameter named ```<id>```.

## Add new item
The form should contain the name of the item, description, like to the image. The form should post to the ```/add-item``` route. You should also generate a unique id for each item (Hint: use random number generator of length 6-8).

After the item was added, redirect the user to the main page.

## Notes
All pages should extend from ```layout.html```.

You should have two classes: ```ItemManager``` (in a separate file).

ItemManager will contain three methods: return all items, find an item (by id) and add a new item to a file.

This class should be separated in its own file. This class should be created once where the Flask application is created and not every time the route is called.