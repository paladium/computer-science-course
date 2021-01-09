# HTTP headers
HTTP headers, allow us to send additional information along with our request. The good thing about http headers is they work for any type of request.

The common use of HTTP headers:
- API key - provided by platform which offers its API for usage
- Content-Type - type of body: json, xml
- Your custom headers: You can set your own headers to send

## Example
To specify headers:
```python
import requests
API_KEY='49f18a19-9c5c-40f8-876b-7f06be9213ae'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'X-CMC_PRO_API_KEY': API_KEY
}
x = requests.get(url, headers=headers)
print(x.json())
```