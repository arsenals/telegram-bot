import csv

import telebot
from telebot import types
TOKEN = '1288453749:AAHy5OsaBLxKOphGl4ai_5fOgoIXnAtG1Ig'
bot = telebot.TeleBot(TOKEN)

entry = {}
inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
btn1 = types.InlineKeyboardButton('income',callback_data = 'income')
btn2 = types.InlineKeyboardButton('casts',callback_data = 'casts')
inline_keyboard.add(btn1,btn2)

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Welcome', reply_markup = inline_keyboard)

@bot.callback_query_handler(func=lambda c:True)
def inline_(c):
    if c.data == 'income':
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard = True)
        btn1 = types.KeyboardButton('Salary')
        btn2 = types.KeyboardButton('FreeLAnce')
        btn3 = types.KeyboardButton('Other')
        income_keyboard.add(btn1, btn2, btn3)
        msg = bot.send_message(c.message.chat.id, 'Choose category', reply_markup=income_keyboard)
        bot.register_next_step_handler(msg, get_category)
    if c.data == 'casts':
        casts_keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True,one_time_keyboard = True)
        btn1 = types.KeyboardButton('Pitanie')
        btn2 = types.KeyboardButton('Komunalnye Uslugi')
        btn3 = types.KeyboardButton('Other')
        casts_keyboard.add(btn1, btn2, btn3)
        msg = bot.send_message(c.message.chat.id, 'Choose category', reply_markup=casts_keyboard)
        bot.register_next_step_handler(msg, get_category)
# if c.data == "costs":
#         costs_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#         btn1 = types.KeyboardButton("Rent a house")
#         btn2 = types.KeyboardButton("Food")
#         btn3 = types.KeyboardButton("Other")
#         costs_keyboard.add(btn1, btn2, btn3)
#         msg = bot.send_message(c.message.chat.id, "Choose category", reply_markup=costs_keyboard)
#         bot.register_next_step_handler(msg, get_category)


def get_category(message):
    chat_id = message.chat.id
    entry['category'] = message.text
    msg = bot.send_message(message.chat.id, 'Input ur sum?')
    bot.register_next_step_handler(msg,get_sum_value)
    print( entry.items())

# def get_category(message):
#     chat_id = message.chat.id
#     entry['category'] = message.text
#     msg2 = bot.send_message(message.chat.id, 'Input ur sum?')
#     bot.register_next_step_handler(msg2,get_sum_value)
#     print( entry.items())

def get_sum_value(message):
    chat_id = message.chat.id 
    entry['sum'] = message.text 
    print(entry.items())

    file_name = 'income.csv'

    with open (file_name, 'a', encoding='UTF -8') as f:
        writer = csv.writer(f)
        writer.writerow((entry.get('category'),entry.get('sum')))
    bot.send_message(chat_id,'Data has been written', reply_markup=inline_keyboard)


bot.polling()