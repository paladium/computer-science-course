import requests
import json

#TODO ask user for username and repo name
username = input("Username : ")
repository = input("Repository : ")
link = 'https://api.github.com' + '/repos' + '/' + username + '/' + repository
response = requests.get(link)
print(response.text)
if response.status_code == 200:
    #Parse response text into json variable, json.loads - string variables, json.load - files
    #Next display the total number of stars and primary language
    data = json.loads(response.text)
    print(data['stargazers_count'])
    print(data['language'])
else:
    print("Not found")