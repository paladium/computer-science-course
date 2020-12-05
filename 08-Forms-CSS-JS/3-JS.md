# Javascript

1. HTML is for content
2. CSS is for presentation
3. JavaScript is for interactivity

- validate user input in an HTML form before sending the data to a server;
- build forms that respond to user input without accessing a server;
- change the appearance of HTML documents and write data to browser Windows;
- open and close new browser windows or frames;
- build small but complete client-side programs.


## Script tag
```html
<html>
<head>
  <title>The Script Tag 1</title>
  <script>
  document.write("<p>Script tags can be placed in the head of an HTML document.</p>");
  </script>
</head>
<body>
  
</body>
</html>
```

Javascript can change the DOM - the rendered HTML, properties, add, remove objects. 
JavaScript can perform requests to the server, without refreshing the page.
In context of bootstrap, JavaScript (Jquery library) can help you make animations, perform form validation, show, hide content etc.

## Short introduction to javascript syntax

Comments:
```js
// Single and multi line comments.
// this is an example of a single line comment.
 
/*
 * this is an example
 * of a
 * multi line
 * comment.
 */
```

Variables:
```js
var a = 4;
let b = "Hello world";
```

Output variables - shows the alert window:
```js
let a = "Hello world";
alert(a);
```

Output variables - console:
```js
let a = "Hello Mars";
console.log(a);
```

Boolean values:
```js
let a = true;
let b = false;
console.log(a == b);
```

Null and undefined:
```js
// Achieve a null value
var foo = null;
// Two ways to achieve an undefined value. 
var bar1 = undefined;
var bar2;
```

if-else if-else:
```js
if ( age < 12 ) {
  entry = "free";
} else if ( age < 18 ) {
  entry = "£10";
} else {
  entry = "£20";
}
```

Loops:
```js
for ( let counter=0; counter < 10; counter++ ) {
   document.write( "<p>" );
   document.write( "Counter is: " + counter );
   document.write( "<p>" );
}

let counter = 0;
while( counter < 10 ) {
   document.write( "<p>" );
   document.write( "Counter is: " + counter );
   document.write( "</p>" );
   counter++;
}
```

Objects:
```js
let a = {
    "name": "test",
    "age": 22,
    "classes": [
        {
            "name": "CS",
            "points": 10
        },
        {
            "name": "Graphics",
            "points": 10
        }
    ]
};
```

JSON:
```js
let a = {
    "name": "test",
    "age": 22,
    "classes": [
        {
            "name": "CS",
            "points": 10
        },
        {
            "name": "Graphics",
            "points": 10
        }
    ]
};
//Convert to json
console.log(JSON.stringify(a));

//Convert json to object
let response = '{"name": "test", "age": 21}';
let b = JSON.parse(response);
console.log(b);
```

Functions:
```js
function hello(name){
    alert("Hello " + name);
}
hello("Ilkin");
```

Arrays:
```js
let images = ["earth.jpg", "mars.jpg", "saturn.jpg"];
console.log(images[0]);
images[1] = "jupiter.jpg";
console.log(images.length);
images.push("mercury.jpg");
```