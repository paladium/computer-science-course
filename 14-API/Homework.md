# SpaceX bot
Create a SpaceX bot, which will have the following commands:
- /latest - return 5 latest flights - title and link
- /launch [id] - return the detailed information about a launch - title, description, total payload and image (attached via Telegram)
- /crew - return all crew members - name of member, image of crew member and link to wikipedia page


## Crypto bot
Create another Telegram bot, which will work with coinmarketcap API to provide information about cryptocurrencies.

It should have the following commands:
- /coins - return 10 top coins (https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest) - with their name, symbol, current price in USD
- /coin-info [symbol:BTC, ETH...] (https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo) - return image, website, title, description, latest price about a given coin
- /coin-price [symbol:BTC, ETH...] (https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest) - return the current price, percent change for 1 hour and 24 hours.