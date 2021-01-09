import telebot
import requests
API_TOKEN = '1577885299:AAF92pueq5O5f6k8UuE-kaXGSE5Rb13lDc8'
API_KEY='49f18a19-9c5c-40f8-876b-7f06be9213ae'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = message.text.split(" ")
    if len(text) == 1:
        bot.reply_to(message, "Please tell me your name")
    else:
        name = text[1]
        bot.reply_to(message, "Hi, how are you doing {}".format(name))

# New command, calculator
# /calculator 4 5
# You need to return the sum of two numbers
# If two numbers are not given, return message enter 2 numbers
@bot.message_handler(commands=['calculator'])
def calculator(message):
    text = message.text.split(" ")
    if len(text) == 1:
        bot.reply_to(message, "Please tell me the numbers")
    elif len(text) == 2:
        bot.reply_to(message, "Please give me two numbers")
    elif len(text) == 3:
        sum = int(text[1]) + int(text[2])
        bot.reply_to(message, "{} + {} equals to {}".format(text[1], text[2], sum))
    else:
        bot.reply_to(message, "Unacceptable number of numbers!")

@bot.message_handler(commands=['wallpaper'])
def send_wallpaper(message):
    chat_id = message.chat.id
    with open('wallpaper.jpg', 'rb') as file:
        bot.send_photo(chat_id, file)

#Response to /get-coin BTC|ETH
#Extract coin name
#API request get to https://pro-api.coinmarketcap.com/v1/cryptocurrency/info
#Add query parameter ?symbol=BTC
#Print json response
@bot.message_handler(commands=['get-coin'])
def get_coin_icon(message):
    text = message.text.split(" ")
    if len(text) == 1:
        bot.reply_to(message, "Please tell me the name of the cryptocurrency")
    else:
        chat_id = message.chat.id
        symbol = text[1]
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol=" + symbol
        headers = {
            'X-CMC_PRO_API_KEY': API_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            image_url = response.json()['data'][symbol]['logo']
            #First way - send the image from the url directly
            r = requests.get(image_url)
            bot.send_photo(chat_id, r.content)
            
            #Second way,if you want to do something with the image, before sending it to the chat
            # with open("{}.png".format(symbol), 'wb') as file:
            #      file.write(r.content)
            # with open('{}.png'.format(symbol), 'rb') as file:
            #      bot.send_photo(chat_id, file)
        else:
            bot.reply_to(message, "Not found!")
    
bot.polling()
