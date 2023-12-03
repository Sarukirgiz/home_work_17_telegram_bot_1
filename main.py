import telebot

from env import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.chat.id, 'hello')
        
@bot.message_handler(commands=['info'])
def start(message):
        bot.send_message(message.chat.id, 'Это тестовый БОТ')      
        
bot.polling()
