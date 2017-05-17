import config
import telebot
from datetime import timedelta

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['uptime'])
def sys(message):
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    bot.reply_to(message, uptime_string)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
