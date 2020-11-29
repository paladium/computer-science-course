# Links
Links are found in nearly all web pages. Links allow users to click their way from page to page.

If you need to provide links on your web page, you need to use the ```a``` tag:
```html
<a href="https://google.com">Google</a>
```
The most important part of the tag is the ```href``` attribute which could be a link on the internet or another html web page locally:
```html
<a href="second.html">Second page</a>
```

You can add a special attribute: ```target``` to change how the link will be opened:
```html
<a href="second.html" target="_blank">Second page</a>
```
```_blank``` means a new browser tab will be opened.