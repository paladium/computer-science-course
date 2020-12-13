# Homework - Extended Online shop
Your online shop from previous homework should now be extended with more features and Flask web server.

It should have 4 pages:
- Main page with all the items
- Individual page for each item
- Login page
- Register page
- Add item page

## Main page
Main page will contain a list of items. Items will be stored in a json file named ```items.json```. This file will be loaded and the data will be sent to the html to render. HTML should render a list of items using ```for``` loop.

## Individual Item
The page for individual item should contain the name, description and the link to the image (link on the internet not local). The id the item to show should be taken from the route parameter named ```<id>```. Also the item should show the username of the user who created it.

## Login page
Login page should contain the username and password field. The form should post to ```/login``` url (use ```url_for``` function). Once logged in, set the cookie with the current username.

## Register page
Register page should contain the username and password field. The form should post to ```/register``` url (use ```url_for``` function). Once successful, redirect the user to login page.

## Add new item
Add new item page, should be shown only if the cookie named ```username``` exists. If not, return the error page to the user (error.html - make it yourself and put custom message inside, like access denied, please login). 

The form should contain the name of the item, description, like to the image. The form should post to the ```/add-item``` route. You should also generate a unique id for each item (Hint: use random number generator of length 6-8).

After the item was added, redirect the user to the main page.

## Notes
All pages should extend from ```layout.html```.

You should have two classes: ```ItemManager``` and ```UserManager``` (in a separate files).

ItemManager will contain three methods: return all items, find an item (by id) and add a new item to a file.

UserManager should have two methods: one to login the user given username and password (return either True or False) and register method, which will take the username and password and add a new user.

These two classes should be separated in their own files. These classes should be created once where the Flask application is created and not every time the route is called.