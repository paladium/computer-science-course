# Img tag
```img``` tag is used to display images in a web page.
This is the simple example of the ```img``` tag:
```html
<img src="images/internet-map.jpg">
```
This will load the image from the same directory as the html located.
```src``` is called an attribute. Attributes are used to set the properties of the tags. ```src``` could be given a link on the internet or a local file on the computer.

If you want to change the size of the image directly in the HTML, you can one of the following attributes: ```width``` and ```height```:
```html
<img src="images/internet-map.jpg" width="200px">
```
We give the value of width in px and the height will be automatically calculated based on the size of the image.

> Important: always put quotes around the values of the attributes.

You can also provide the ```alt``` attribute to the image to help browsers understand what is the image about:
```html
<img src="images/internet-map.jpg" width="200px" alt="Internet map">
```