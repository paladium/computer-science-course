# DOM manipulation using JS
When a web page is loaded, the browser creates a Document Object Model of the page.

The HTML DOM model is constructed as a tree of Objects:
![dom](./img/dom.gif)

With the object model, JavaScript gets all the power it needs to create dynamic HTML:

- JavaScript can change all the HTML elements in the page
- JavaScript can change all the HTML attributes in the page
- JavaScript can change all the CSS styles in the page
- JavaScript can remove existing HTML elements and attributes
- JavaScript can add new HTML elements and attributes
- JavaScript can react to all existing HTML events in the page
- JavaScript can create new HTML events in the page

## Get element
The following example changes the content (the innerHTML) of the <p> element with id="demo":
```html
<html>
<body>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "Hello World!";
</script>

</body>
</html>
```

In the example above, ```getElementById``` is a method, while ```innerHTML``` is a property.


More ways to get the element: https://www.w3schools.com/js/js_htmldom_document.asp (by css-class)

## Events
We can use HTML events (mouse click, hover) and execute custom logic in javascript.

When clicking on the button, the image is changed:

```html
<html>
    <head>
    </head>
    <body>
        <img id="image" src="./earth.jpg">
        <button id="changeImage">Change image</button>
        <script>
            let button = document.getElementById("changeImage");
            let image = document.getElementById("image");
            button.addEventListener("click", function(){
                image.src = "./mars.jpg";
            });
        </script>
    </body>
</html>
```

Or the following example, checks whether the username is available:
```html
<html>
    <head>
    </head>
    <body>
        <input name="username" id="username" placeholder="Username"/>
        <button id="checkUsername">Check username</button>
    </body>
    <script>
            let button = document.getElementById("checkUsername");
            let usernameInput = document.getElementById("username");
            function checkUsername(){
                let registeredUsernames = ["tesla-cool", "elon-musk", "mars"];
                let username = usernameInput.value;
                let usernameExists = false;
                for(var i=0;i<registeredUsernames.length;i++){
                    if(registeredUsernames[i] == username){
                        usernameExists = true;
                        break;
                    }
                }
                if(usernameExists){
                    alert("Please choose a different username");
                }
            }
            button.addEventListener("click", checkUsername);
    </script>
</html>
```