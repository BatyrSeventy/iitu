""" Echo bot. Done by Zhetpisbayev Batyrzhan """
import telebot


token = "251725356:AAH6bUZRfdaMp8OhaY-CdlL5zuJVJoOUUBY"
bot = telebot.TeleBot(token)
welcome_text = "Howdy!\n\nAviable commands:\n/start - start"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, welcome_text)


def start_bot():
    print("Bot started...")
    bot.polling(none_stop=True)

start_bot()
