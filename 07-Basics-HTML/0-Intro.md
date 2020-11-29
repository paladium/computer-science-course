# Introduction to HTML - Hyper Text Markup Language

- HTML is the standard markup language for creating Web pages
- HTML describes the structure of a Web page
- HTML consists of a series of elements
- HTML elements tell the browser how to display the content

HTML on the OSI model is Level 7 (Application layer), which means that underlying layers do not really care what is being transferred - html, images, video, the application that requests those resources from the server is responsible for parsing and understanding how to display them.

Every file has a format and application that can open it, for example .png can be opened by image viewer or docx can be opened by word. HTML is also a file format and the application that opens it is the web browser.

> Remember: HTML tells the browser which content to put on the page and CSS tells how to put that content (position, style etc.)

Every web page that you open is rendered using HTML.

## Simple HTML
This is the example of the simplest HTML web-page:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        Hello world
    </body>
</html>
```
Let's understand it piece by piece:
- The ```<!DOCTYPE html>``` declaration defines that this document is an HTML5 document
- HTML is a subset of XML, meaning it has the same syntax. Everything happens using tags: html, head, title, body. Each tag should open a close (except img tag).
- HTML starts with html tag as the root, then it has the head (which is used by the browser for things like tab icon, title)
- Title tag displays the title of our page in the browser tab
- The main part of the HTML is the body. Body is where you put the content of your page, you can place images, videos, text, other web pages, etc.

We can now open that page in browser and view it.


## Text tags
There are different standard tags available in HTML:
1. ```h1``` - top-level header, usually used for the title of the article, page etc.
2. ```h2``` - second level header, usually subpart
3. ```h3``` - third level header
4. ```h4``` - fourth level header
5. ```h5``` - fifth level header
6. ```h6``` - sixth level header

Headings are important for your page, as Google and other search engines use them to understand what your content is about.

When you want to display a paragraph, there is a tag for that: ```p```, it displays a piece of text.
