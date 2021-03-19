import telebot
import config
import random

from telebot import types

TOKEN = '982809373:AAGQIosPzMXjaMXUUovYmw3kmDfFcBXWrRA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton("Python-это")
	item2 = types.KeyboardButton("Интересное")
	
	markup.add(item1, item2)
	
	hi = open('ph/sa.webp', 'rb')
	bot.send_sticker(message.chat.id, hi)
	bot.send_message(message.chat.id, "Хай!", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Python-это':
			markup = types.InlineKeyboardMarkup(row_width=2)	
			item1 = types.InlineKeyboardButton("Понял давай дальше!", callback_data='good')
			item2 = types.InlineKeyboardButton("Можно подробнее", callback_data='bad')
			markup.add(item1, item2)			

			bot.send_message(message.chat.id, 'Python - высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен. В то же время стандартная библиотека включает большой объём полезных функций.', reply_markup=markup)
		elif message.text == 'Интересное':
			role = random.randint(0,1)
			if role==0:
				oo = open('ph/st.webp', 'rb')
				bot.send_sticker(message.chat.id, oo)		
				bot.send_message(message.chat.id, 'Это метод send_sticker из PyTelegramBotApi - библиотеки для ратоты с ботом телеграм с помощью языка Python')
			elif role==1:
				rx = open('ph/rr.webp', 'rb')
				bot.send_photo(message.chat.id, rx)
				bot.send_message(message.chat.id, 'Это метод send_photo из PyTelegramBotApi - библиотеки для ратоты с ботом телеграм с помощью языка Python')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				markup = types.InlineKeyboardMarkup(row_width=2)	
				item1 = types.InlineKeyboardButton("Табуляция", callback_data='a')
				item2 = types.InlineKeyboardButton("Массивы", callback_data='b')
				item3 = types.InlineKeyboardButton("Ветвление", callback_data='c')
				markup.add(item1, item2, item3)
			
				bot.send_message(call.message.chat.id, 'Что дальше', reply_markup=markup)
			elif call.data == 'bad':
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton("Табуляция", callback_data='a')
				item2 = types.InlineKeyboardButton("Массивы", callback_data='b')
				item3 = types.InlineKeyboardButton("Ветвление", callback_data='c')
				markup.add(item1, item2, item3)

				sti = open('ph/zhiv.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				bot.send_message(call.message.chat.id, 'Хороший краткий гайд: https://www.youtube.com/watch?v=fp5-XQFr_nk&t=418s&pbjreload=10', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'a':
				markup = types.InlineKeyboardMarkup(row_width=2)	
				item1 = types.InlineKeyboardButton("Пример", callback_data='a')
				item2 = types.InlineKeyboardButton("Задача", callback_data='b')
				markup.add(item1, item2, item3)

				bot.send_message(call.message.chat.id, 'Ветвление — алгоритмическая конструкция, в которой, в зависимости от результата проверки условия («да» или «нет»), предусмотрен выбор одной из двух последовательностей действий (ветвей). Гайд по ветвлению Python: https://habr.com/ru/post/50120/', reply_markup=markup)

	except Exception as e:
		print(repr(e))


bot.polling(none_stop=True)