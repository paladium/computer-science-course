import requests
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'test', 
    'body': 'cool', 
    'userId': 1
}
x = requests.post(url, json=data) 
print(x.content)
print(x.json())