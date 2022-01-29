# from cgitb import handler
# from urllib import response
from http.client import responses
import Constants as keys
from telegram.ext import *
import responces as R
print("bot started")

def start(update, context):
    update.message.reply_text("type anything to start")
    
def helpwe(update, context):
    update.message.reply_text("type to need help")
    
def handle(update, context):
    text = str(update.message.text).lower()
    response = R.sampleresponses(text)
    update.message.reply_text(response)

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("helpwe", helpwe))
    dp.add_handler(MessageHandler(Filters.text, handle))
    updater.start_polling()
    updater.idle()
    
    
main()