import os
import telepot
from telepot.loop import MessageLoop
from keep_alive import keep_alive

# Define the token
TOKEN = os.environ.get('7135600634:AAGiMAyfJ5HCnAqaVTcQH4Zj3GzhH10_szU')

# Define the start command handler
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, "Hello! I'm Gunther Bot, pleased to meet you!")
        else:
            bot.sendMessage(chat_id, "I don't understand this command.")

# Create the bot instance
bot = telepot.Bot(TOKEN)

# Start the message loop
MessageLoop(bot, handle).run_as_thread()

# Keep the bot running
keep_alive()

# Keep the program running
import time
while True:
    time.sleep(10)
