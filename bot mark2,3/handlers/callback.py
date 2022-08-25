from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_2(call: types.CallbackQuery):
    mark_up = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("NEXT question", callback_data='button2')
    mark_up.add(button2)

    question = "who's your president?"
    answers = [
        'Michael Jordan',
        'Anjelina Jolie',
        'your mom',
        'Sadyr Japarov',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        reply_markup=mark_up
    )


async def quiz_3(call: types.CallbackQuery):
    mark_up = InlineKeyboardMarkup()
    button3 = InlineKeyboardButton("NEXT question", callback_data='button3')
    mark_up.add(button3)

    question = "Best OS in the world"
    answers = [
        'Windows',
        'MacOS',
        'Ubuntu Linux',
        'Red Hat Enterprise Linux',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=mark_up
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button2')

