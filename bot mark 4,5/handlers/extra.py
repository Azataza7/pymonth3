from aiogram import types, Dispatcher
from config import bot, ADMIN
import random


async def mem(message: types.Message):
    photo = open('media/2zxmg9.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def commands(message: types.Message):
    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        return
    if message.text.lower().startswith('game') and message.from_user.id in ADMIN:
        start_game = random.choice(['⚽', "🏀", "🎲", "🎯", "🎳", "🎰"])
        await bot.send_dice(message.chat.id, emoji=start_game, reply_to_message_id=start_game)


async def square(message: types.Message):
    if message.text.isdigit():
        message.text = int(message.text)
        message.text **= 2
        await bot.send_message(message.from_user.id, message.text)
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_message_handler_extra(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(commands)
    dp.register_message_handler(square)


