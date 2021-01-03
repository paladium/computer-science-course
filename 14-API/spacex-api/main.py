#Get a list of all the lauches and parse it into json variable
import requests
import json
import matplotlib.pyplot as plt

link = "https://api.spacexdata.com/v4/launches/"

response = requests.get(link)

launches = json.loads(response.text)

x = []
y = []
n = 1

for launch in launches:
    launch['total_mass'] = 0
    for payload in launch['payloads']:
        link2 = "https://api.spacexdata.com/v4/payloads/" + payload
        response = requests.get(link2)
        payload_data = json.loads(response.text)
        if payload_data['mass_kg']:
            launch['total_mass'] += payload_data['mass_kg']
    print(n)
    n += 1
    x.append(launch['name'])
    y.append(launch['total_mass'])

plt.scatter(x, y, marker='o')

plt.xlabel('Launches') 
# naming the y axis 
plt.ylabel('Total mass') 
  
# giving a title to my graph 
plt.title('Total mass per launch') 
  
# function to show the plot 
plt.show() 