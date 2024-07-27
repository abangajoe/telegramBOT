import os
import telepot
import logging
from telepot.loop import MessageLoop
from keep_alive import keep_alive

logging.basicConfig(level=logging.INFO)
TOKEN = '7135600634:AAGiMAyfJ5HCnAqaVTcQH4Zj3GzhH10_szU'
bot = telepot.Bot(TOKEN)

pdf_files = {
    "effective prayer": "files/Effective Prayer - Charles Spurgeon.pdf",
    "freedom from pornography":"files/Freedom From Pornography 25062024.pdf",
    "what the bible says about the holy spirit": "files/What the Bible Says About the Holy Sp... (Z-Library).pdf",
    "weapons of spritual welfare": "files/Weapons of spritual welfare.pdf",
    "tozer_gems": "files/A.W. Tozer_Gems from Tozer.pdf",
    "knowledge of the holy": "files/A.W.Tozer - Knowledge of The Holy.pdf",
    "god's pursuit of man": "files/God's Pursuit of Man - AW Tozer-1.pdf",
    "how to hear gods voice": "files/How to Hear Gods Voice (Mark Virkler... (Z-Library).pdf",
    "lights in the sky": "files/Lights in the Sky  Little Green Men A... (Z-Library).pdf",
    "making disciples": "files/Multiply disciples making disciples (... (Z-Library).pdf",
    "operation joktan": "files/Operation Joktan - Nir Tavor Series 0... (Z-Library).pdf",
    "power moves": "files/Power Moves (Sarah Jakes Roberts) (Z-Library).pdf",
    "success is a choice": "files/Success-Is-a-Choice.PDF",
    "the making of a watchman": "files/The Making of a Watchman Practical Tr... (Z-Library).pdf",
    "walking with god": "files/vdoc.pub_walking-with-god-talk-to-him-hear-from-him-really.pdf",
    "voice of a prophet": "files/Voice of a Prophet_ Who Speaks - A. W. Tozer.pdf",
    "what the bible says about praying": "files/What_the_Bible_Says_about_Praying_by_Hudson,_Christopher_D_z_lib.pdf",
    "moral monster.pdf": "files/1608.pdf",
    "meet a marriage": "files/Created To Need A Help Meet A Marriag... (Z-Library).pdf",
    "defying jihad": "files/Defying Jihad by Esther Ahmad.pdf",
    "eusebius and empire": "files/Eusebius and Empire Constructing Chur... (Z-Library).pdf",
    "following the path of the eagle": "files/Following the path of the eagle (Davi... (Z-Library).pdf",
    "hermeneutics, inerrancy, and the bible": "files/Hermeneutics, Inerrancy, and the Bibl... (Z-Library).pdf",
    "in pusuit of vision (david o. oyedepo)": "files/IN PUSUIT OF VISION (David O. Oyedepo) (Z-Library).pdf",
    "martin hengel crucifixion in the ancient world": "files/Martin_Hengel_Crucifixion_in_the_Ancient_World_and_the_Folly_of.pdf",
    "no god but one allah or jesus": "files/No God but One Allah or Jesus by Nabeel Qureshi.pdf",
    "redeeming mathematics a god centered approach": "files/Redeeming_Mathematics_A_God_Centered_Approach_Vern_S_Poythress.pdf",
    "redeeming science a god centered approach": "files/Redeeming_Science_A_God_Centered_Approach_Vern_Sheridan_Poythress.pdf",
    "seeking allah, finding jesus": "files/Seeking_Allah,_Finding_Jesus_A_Devout_Muslim_Encounters_Christianity.pdf",
    "the power of a praying parent": "files/The Power of a Praying Parent - Stormie Omartian.pdf",
    "understanding divine direction": "files/UNDERSTANDING DIVINE DIRECTION (David... (Z-Library).pdf",

}

video_files = {
    "lauren daigle": "files/Lauren Daigle - You Say (Official Music Video).mp4",
}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    try:
        if content_type == 'text':
            text = msg['text'].lower()

            if text in ["hi", "hello", "hey"]:
                bot.sendMessage(chat_id, "This is Umat AGCM bot. How may I help you")
                
            elif text == "/list_pdfs" or text.lower() == "list of pdfs":
                pdf_list = "\n".join(pdf_files.keys())
                bot.sendMessage(chat_id, "YOU CAN ACCESS THE FOLLOWING BOOKS:\n" + pdf_list) 
                
            elif text == "/list_videos" or text.lower() == "list of videos":
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
