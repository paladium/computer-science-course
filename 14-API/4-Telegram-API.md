# Telegram API
Telegram offers its API for developers to create Telegram bots - applications which can answer the messages in the chat, send images, videos etc.

We are going to be using a special library - wrapper around Telegram API. The reason we are using library and not raw API is due to complexity of different methods available, especially with responding to real-time messages. However, most of the concepts we studied around API, applies here as well.

## Getting started
First we need to install the library:
```bash
pip install pyTelegramBotAPI
```

Next we should grab a Token from BotFather. Find BotFather in your Telegram and follow the instructions to get the token.

Finally, let's use our token and answer some commands:
```python
import telebot
API_TOKEN = 'your-token'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi, how are you doing?")

bot.polling()
```