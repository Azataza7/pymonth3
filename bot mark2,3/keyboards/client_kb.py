from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_button = KeyboardButton('/start')
mem_button = KeyboardButton('/mem')
quiz_button = KeyboardButton('/quiz')
info_button = KeyboardButton('Share contact', request_contact=True)

start_markup.row(mem_button, quiz_button, info_button)

cancel_button = KeyboardButton("Cancel")
cancel_markup = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True
).add(cancel_button)

