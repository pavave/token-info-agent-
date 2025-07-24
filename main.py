import telebot
import os
from dotenv import load_dotenv
from token_utils import get_token_price

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hi! I'm Token Info Agent.\nAsk me the price of any token like:\n• What's the price of ETH?\n• How much is SHIBA?\n• Price of PEPE?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    response = get_token_price(user_input)
    bot.reply_to(message, response)

bot.polling()
