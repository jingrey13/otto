from telegram.ext import Updater, CommandHandler

def start(bot, update):
update.message.reply_text('Hello World!')

def hello(bot, update):
update.message.reply_text(
'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('415048379:AAHoccZk9RPZll17K2mroxTp3U7qMl9s3sg')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
