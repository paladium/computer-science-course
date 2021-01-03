# API requests in Python
Just like having a web server with GET and POST methods, we can also request data from API using GET method and send data using POST method.

We will using ```requests``` library that makes working with API really easy:
```bash
pip install requests
```
Next let's make our first request:
```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.text)
```

## More examples
Let's use SpaceX api to get the list of flights (https://github.com/r-spacex/SpaceX-API). We first get the link to flights:
```python
link = "https://api.spacexdata.com/v4/launches/"
```
Now we can make the GET request:
```python
response = requests.get(link)
print(response.text)
```
Now we can combine it with ```json``` package to parse the data:
```python
import json
flights = json.loads(response.text)
```
Now ```flights``` object will contain a list of flights sorted by date. We can use that data for any purpose:
- Send data to a private telegram channel
- Save the data to our own JSON file and use for later processing
- Use matplotlib library to display the weight of payloads


## Graphs in Python
To start working with graphs, we need to install this library:
```bash
pip install matplotlib
```

Next let's display our first graph:
```python
# importing the required module 
import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 

# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 
```