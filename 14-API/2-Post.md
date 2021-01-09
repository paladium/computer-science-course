# API Post requests
GET requests allow us to retrieve information. 

However when working with real-world API, it is often required not only to get information, but to create it.

That is where POST requests comes in. It works the same way as Flask post request and allow us you to send data in body (manually without the need of html).

## Example
```python
import requests
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'test', 
    'body': 'cool', 
    'userId': 1
}
x = requests.post(url, json=data) 
print(x.content)
``