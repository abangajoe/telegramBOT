import os
import telepot
import logging
from telepot.loop import MessageLoop
from keep_alive import keep_alive

logging.basicConfig(level=logging.INFO)
TOKEN = '7135600634:AAGiMAyfJ5HCnAqaVTcQH4Zj3GzhH10_szU'
bot = telepot.Bot(TOKEN)

pdf_files = {
    "effective prayer": "Effective Prayer - Charles Spurgeon.pdf",
}

video_files = {
    "lauren daigle": "Lauren Daigle - You Say (Official Music Video).mp4",
}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    try:
        if content_type == 'text':
            text = msg['text'].lower()

            if text in ["hi", "hello", "hey"]:
                bot.sendMessage(chat_id, "This is Umat AGCM bot. How may I help you")
                
            elif text == "/list_pdfs":
                pdf_list = "\n".join(pdf_files.keys())
                bot.sendMessage(chat_id, "YOU CAN ACCESS THE FOLLOWING BOOKS:\n" + pdf_list) 
                
            elif text == "/list_videos":
                video_list = "\n".join(video_files.keys())
                bot.sendMessage(chat_id, "YOU CAN ACCESS THE FOLLOWING VIDEOS:\n" + video_list)
                
            elif text in pdf_files:
                bot.sendDocument(chat_id, open(pdf_files[text], 'rb'))
                
            elif text in video_files:
                bot.sendVideo(chat_id, open(video_files[text], 'rb'))
                
            else:
                bot.sendMessage(chat_id, "I'm a limitted bot, Please try again with familiar commands.")


    except Exception as e:
        logging.error(f"Error handling message: {e}")
        bot.sendMessage(chat_id, "An error occurred while processing your request. Please try again later.")


MessageLoop(bot, handle).run_as_thread()

# Keep the bot running
keep_alive()

# Keep the program running
import time
while True:
    time.sleep(10)
