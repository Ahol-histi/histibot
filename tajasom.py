import telebot
import random

list_rond = [
    "اشتباهه، چرا بیشتر فکر نمیکنی",
    "نچ نچ نچ، صورتم بخاطرت گریون شده",
    "انگار سوار چرخ و فلکی، هی هی و هی دور خودت میچرخی",
    "اصلاً به چیزایی که دیدی نگاه کردی؟ بیشتر فکر کن"
]

list_rond_phase2 = [
    "درکت میکنم! معمای عجیبیه", "یادته گفتم به چیزایی که گفتم نگاه کن؟ تارگتت حروفن واقعا اینجا؟", "آه پسر چند ساعته علافتم"
]

TOKEN = "7996532529:AAHiX5gTrRUaLAMH8uz8TzSAlKqRfqzGwA0"
bot = telebot.TeleBot(TOKEN)

user_phase = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_phase[message.chat.id] = 1  
    bot.reply_to(message, "If you found the answer, well done, it's time to enter it here so you can move on to the next world:")

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    user_id = message.chat.id
    current_phase = user_phase.get(user_id, 1) 

    if current_phase == 1:
        if message.text.strip().lower() == "big dipper":
            bot.reply_to(message, "great! now, think: I've been stuck on level 30 for 12 hours, all because of my left hand. What's my name in this situation?")
            user_phase[user_id] = 2  
        else:
            bot.reply_to(message, random.choice(list_rond))
    
    elif current_phase == 2:
        
        if message.text.strip().lower() == "dexter":
            bot.reply_to(message, "send (hasti) to He_ridam in telegram and get your gift")
            
            user_phase[user_id] = 1  
        else:
            bot.reply_to(message, random.choice(list_rond_phase2))

bot.infinity_polling()