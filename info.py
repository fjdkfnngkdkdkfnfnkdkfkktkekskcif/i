import telebot
import requests
from telebot import *
token = input('[=] Enter Token : ')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id,f"""<strong>
[+] IɴsᴛᴀGʀᴀᴍ Iɴғᴏ
</strong>""",parse_mode="html")
    bot.reply_to(message,"<strong>[+] Sᴇɴᴅ UsᴇʀNᴀᴍᴇ  ✅ </strong>",parse_mode="html")
    @bot.message_handler(func=lambda message: True)
    def start(message):
        userQ = message.text
        if userQ != "qwertyuioplkjhgfdsazxcvbnm0987654321" : 
            link = (f"https://www.instagram.com/{userQ}/")
            bot.send_message(message.chat.id,text = "<strong>[+] Wᴀɪᴛ Pʟᴇᴀsᴇ ⏱ ..</strong>",parse_mode="html")
            url = (f"https://soud.me/api/Instagram?username={userQ}")
            sd = requests.get(url).json()
            stud = sd['message']
            if stud=="User Found" :
                edge_followed_by = sd["info"]["followers"]
                edge_follow = sd["info"]["following"]
                id = sd["info"]["id"]
                png1 = sd["info"]["image"]
                bio60 = sd['info']['bio']
                posts = sd['info']['media']
                namep = sd['info']['name']
                png = (png1)
                url00 = (f"https://o7aa.pythonanywhere.com/?id={id}")
                sd00 = requests.get(url00).json()
                data0 = sd00['data']
                bot.send_message(message.chat.id,f"""<strong>
[+] UsᴇʀNᴀᴍᴇ : {userQ}
[+] Fᴏʟʟᴏᴡᴇʀs : {edge_followed_by}
[+] Fᴏʟʟᴏᴡɪɴɢ : {edge_follow}
[+] Nᴀᴍᴇ : {namep}
[+] Dᴀᴛᴇ : {data0} 
[+] Pᴏsᴛ : {posts}
[+] ID : {id}
[+] Bɪᴏ : {bio60}
-   -   -   -   -  -  -  -  -  -  -   -   - 
    </strong>""",parse_mode="html")
                bot.reply_to(message,"<strong>[+] Sᴇɴᴅ UsᴇʀNᴀᴍᴇ  ✅ </strong>",parse_mode="html")
            else :
                bot.reply_to(message,"<strong>[+] UsᴇʀNᴀᴍᴇ Eʀʀᴏʀ ❎ </strong>",parse_mode="html")
                bot.send_message(message.chat.id,text = "<strong>[+] Pʟᴇᴀsᴇ Tʀʏ Aɢᴀɪɴ </strong>",parse_mode="html")

bot.polling(True)