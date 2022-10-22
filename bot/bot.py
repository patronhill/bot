from email import message
import requests
from datetime import datetime
import telebot 
from config import token
import random
from parser import urls


now = datetime.now().strftime('%Y-%m-%d %H:%M')
imag = [
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F0.gif?alt=media&token=0fff4b31-b3d8-44fb-be39-723f040e57fb",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F1.gif?alt=media&token=2328c855-572f-4a10-af8c-23a6e1db574c",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F10.gif?alt=media&token=647fd422-c8d1-4879-af3e-fea695da79b2",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F11.gif?alt=media&token=900cce1f-55c0-4e02-80c6-ee587d1e9b6e",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F2.gif?alt=media&token=8a108bd4-8dfc-4dbc-9b8c-0db0e626f65b",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F3.gif?alt=media&token=4e270d85-0be3-4048-99bd-696ece8070ea",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F4.gif?alt=media&token=e7daf297-e615-4dfc-aa19-bee959204774",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F5.gif?alt=media&token=a8e472e6-94da-45f9-aab8-d51ec499e5ed",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F7.gif?alt=media&token=9e449089-9f94-4002-a92a-3e44c6bd18a9",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F8.gif?alt=media&token=80a48714-7aaa-45fa-a36b-a7653dc3292b",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F9.gif?alt=media&token=a57a1c71-a8af-4170-8fee-bfe11809f0b3",
]


def get_data():
    req = requests.get('https://cdn.cur.su/api/latest.json')
    response = req.json()
    sell_price = response["rates"]["AMD"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Sell AMD price: {sell_price}")
    


def telegram_bot(token):
    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=["start"])
    
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! write the 'price' to find out the cost of AMD!\n We have Paster eggs with 'Cats'!!!")  

    @bot.message_handler(content_types=["text"])      
    def sen_text(message):
        if message.text.lower() == "\/price":
            bot.reply_to(message, 'Please write the number of $$$') 
        
        elif  message.text.isdigit():
            try:
                    y = float(message.text)
                    req = requests.get('https://cdn.cur.su/api/latest.json')
                    response = req.json()
                    sell_price = response["rates"]["AMD"]
                    sell_price1 = y * sell_price 
                    bot.send_message(
                         message.chat.id,
                        f"{now}\n Sell AMD price: {sell_price1}"
                         )
            except Exception as ex:
                    print(ex)    
                    bot.send_message(
                    message.chat.id,
                    "API doesn't work!!!")
                
            bot.send_message(
                message.chat.id,
                "Tres bien mon ami")
        elif message.text.lower() in ("котики" , "cat" , "pussy" , "кошка" , "cats" , "киски"):
            bot.send_animation(message.chat.id, random.choice(imag))  
        elif message.text.lower() in ('\/work'):
            bot.send_message(message.chat.id, random.choice(urls))       
        else: 
            bot.send_message(message.chat.id,'nice')

    bot.polling()
   

if __name__ == '__main__':
    #get_data()
    telegram_bot(token)
    

