import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, Updater
from keep_alive import keep_alive

keep_alive()

bot = Bot(token=os.environ.get('TOKEN'))
updater = Updater(bot=bot, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    updater.start_polling()
