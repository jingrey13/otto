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
    if string.upper()[:3] == "BYE":
        bot.sendMessage(chat_id=update.message.chat_id, text='Bye '+update.message.from_user.first_name+'!')    
def subscribe(bot, update):
    userid = update.message.from_user.username + '\n'
#    bot.sendMessage(chat_id=update.message.chat_id, text=userid)
    sub_file = open("subscriberlist.txt", "r")
    sublist = sub_file.readlines()
    sub_file.close()
    yes_flag = 0
    for i, x in enumerate(sublist):
        if sublist[i] == userid:
            yes_flag = 1
    if yes_flag == 0:
        bot.sendMessage(chat_id=update.message.chat_id, text=userid)
        fh = open("subscriberlist.txt", "a")
        fh.write(userid)
        fh.close()
def pingall(bot,update):
    chatid = update.message.chat.id
    #update.effective_message.reply_text(chatid)
    if chatid == jinotto:
        sub_file = open("subscriberlist.txt", "r")
        sublist = sub_file.readlines()
        sub_file.close()
        sublist = [s.replace('\n', '') for s in sublist]
        name = update.message.from_user.first_name
        pretext= ' wants to play a game. Where is everybody?\n\n'
        j=0
        combined_msg= name + pretext
        for x in sublist:
            combined_msg = combined_msg + '@' + x + '\n'
        bot.sendMessage(chat_id=update.message.chat_id, text=combined_msg)
        del sublist[:]
def inspire(bot,update,job_queue):
    global inspiretime
    if inspiretime == 0:
        url = "http://inspirobot.me/api?generate=true"
        r = requests.get(url)
        quote = r.text
        bot.sendMessage(chat_id=update.message.chat_id, text=quote)
        inspiretime = 1
        job_queue.run_once(resetinspire, 60, context=update.message.chat_id)
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='We are inspired enough for now. Please wait.')
def resetinspire(bot, job):
    global inspiretime
    inspiretime = 0
#def resettimer(bot, update, job_queue):
#    bot.sendMessage(chat_id=update.message.chat_id, text='Wait')
#    job_queue.run_once(inspire, 0, context=update.message.chat_id)
#    job_queue.run_once(resetinspire, 60, context=update.message.chat_id)

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
  #  j = updater.job_queue
    # Add handlers
#    dp.add_handler(CommandHandler('start', start))
#    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('sub', subscribe))
    dp.add_handler(CommandHandler('ping', ping))
    dp.add_handler(CommandHandler('hi', hi))
#    dp.add_handler(MessageHandler(Filters.text, greeting))
    dp.add_handler(CommandHandler('pingall', pingall))
#    dp.add_handler(CommandHandler('inspire', inspire))
    dp.add_handler(CommandHandler('inspire', inspire, pass_job_queue=True))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
