import requests
API_KEY='49f18a19-9c5c-40f8-876b-7f06be9213ae'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'X-CMC_PRO_API_KEY': API_KEY
}
x = requests.get(url, headers=headers)
print(x.json())