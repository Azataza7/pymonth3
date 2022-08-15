
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import dp, bot


@dp.message_handler(commands=['quiz'])
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
        open_period=9000,
        reply_markup=mark_up
    )


@dp.callback_query_handler(lambda call: call.data == 'button1')
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


@dp.callback_query_handler(lambda call: call.data == 'button2')
async def quiz_2(call: types.CallbackQuery):
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


@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('2zxmg9.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        message.text = int(message.text)
        message.text **= 2
        await bot.send_message(message.from_user.id, message.text)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
