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

## Homework - Simple chat
Create a simple chat using HTML and JavaScript and Bootstrap. The chat will have two pages - login and chat.

## Login page
Login page will contain the form to enter the username and password of the user. Using javascript only, verify whether the username and password both equal to the value "admin". If they are, you should redirect the user to the chat page (/chat.html, for that you need to use the command window.location.href = "/chat.html" to programatically navigate to another page).

If the credentials are invalid, show an alert to the user.

## Chat page
The chat page, will contain a single textarea element (readonly) with all the chat between the user and the bot.

Also at the bottom, there should be an input element to send the text and the button to send the message.

Once the button to send the message is clicked, the message is appended to the textarea by adding to its value.

Finally, the bot should have a simple logic to communicate with the user.

Use the following structure of the "brain" of the bot:
```json
[
    {
        "messages": [
            "Hello",
            "Hi",
            "Good morning"
        ],
        "response": "Hello, how are you?"
    },
    {
        "messages": [
            "How old are you?",
            "What is your age?"
        ],
        "response": "I am just a bot without an age"
    }
]
```
So when the user enters the message "Hello" or "Hi", you should return the response to the user by also appended the text to the textarea.

Note: you can use the function toLowerCase to convert the user input to lowercase to make sure, you always get some response.