import os

API_TOKEN = os.environ.get("API_TOKEN")

if API_TOKEN is None:
    print("Token is not given")
else:
    print(API_TOKEN)