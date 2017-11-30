import requests
import logging
import os
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

jinotto = 114698280
secrethitler = -1001100171347
inspiretime = 0

def start(bot, update):
    update.effective_message.reply_text("Hi!")
def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)
def ping(bot, update):
    update.effective_message.reply_text("I'm alive! =D")
def hi(bot, update):
    name = update.message.from_user.first_name
    name2 = update.message.from_user.last_name
    update.effective_message.reply_text("Hi there "+name)
def greeting(bot, update):
    chatid = update.message.chat.id
    string = update.effective_message.text
    if string.upper()== "HI":
        bot.sendMessage(chat_id=update.message.chat_id, text='Hi '+update.message.from_user.first_name+'!')
    if string.upper()[:3] == "HI ":
        bot.sendMessage(chat_id=update.message.chat_id, text='Hi '+update.message.from_user.first_name+'!')
    if string.upper()[:3] == "HIH":
        bot.sendMessage(chat_id=update.message.chat_id, text='Hi '+update.message.from_user.first_name+'!')
    if string.upper()[:3] == "HI!":
        bot.sendMessage(chat_id=update.message.chat_id, text='Hi '+update.message.from_user.first_name+'!')
    if string.upper()[:5] == "HELLO":
        bot.sendMessage(chat_id=update.message.chat_id, text='Hi! '+update.message.from_user.first_name+'!')
    if string.upper()[:7] == "MORNING":
        bot.sendMessage(chat_id=update.message.chat_id, text='Morning '+update.message.from_user.first_name+'!')
    if string.upper()[:7] == "BYE":
        bot.sendMessage(chat_id=update.message.chat_id, text='Bye '+update.message.from_user.first_name+'!')    
def pingall(bot,update):
    chatid = update.message.chat.id
    #update.effective_message.reply_text(chatid)
    if chatid == secrethitler:
        name = update.message.from_user.first_name
        bot.sendMessage(chat_id=update.message.chat_id, text=name+' wants to play a game. Where is everybody?\n@edddddyyyy\n@Meowcolm\n@Reinaku\n@JeriKokHo\n@Nnavi92\n@pamelatay\n@Haoward\n@JinGrey13')
def inspire(bot,update):
    if inspiretime == 0:
        url = "http://inspirobot.me/api?generate=true"
        r = requests.get(url)
        quote = r.text
        bot.sendMessage(chat_id=update.message.chat_id, text=quote)
        inspiretime = 1
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="We are inspired enough for now. Please wait.")
def resetinspire(bot, job):
    inspiretime = 0
def resettimer(bot, update, job_queue):
    job_queue_run_once(resetinspire, 60, context=update.message.chat_id)

if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "415048379:AAHoccZk9RPZll17K2mroxTp3U7qMl9s3sg"
    NAME = "hidden-sea-92222"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    j = dp.job_queue
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    #dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('ping', ping))
    dp.add_handler(CommandHandler('hi', hi))
    dp.add_handler(MessageHandler(Filters.text, greeting))
    dp.add_handler(CommandHandler('pingall', pingall))
    dp.add_handler(CommandHandler('inspire', inspire))
    dp.add_handler(CommandHandler('inspire', timerreset, pass_job_queue=True))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
