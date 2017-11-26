from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
