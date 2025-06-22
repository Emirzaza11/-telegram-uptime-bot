import telebot
from keep_alive import keep_alive

API_TOKEN = 'BURAYA_BOT_TOKENINI_YAZ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selam! Ben Railway'de 7/24 çalışıyorum 🚀")

keep_alive()

bot.polling()
