from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards import client_kb


async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello!{message.from_user.full_name}",
                           reply_markup=client_kb.start_markup)


async def quiz_1(message: types.Message):
    mark_up = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("NEXT question", callback_data='button1')
    mark_up.add(button1)
    questions = 'Who start war in Ukraine?'
    answers = [
        'Putin',
        'Putin chmo',
        'USA',
        'Kyrgyzstan',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=mark_up
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])



