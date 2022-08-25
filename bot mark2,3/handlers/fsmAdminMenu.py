from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboards.client_kb import cancel_markup


class FSMAdmin(StatesGroup):
    photo = State()
    food_name = State()
    description = State()
    food_cost = State()
    energy_value = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.photo.set()
        await message.answer(f'Добро пожаловать в кафе у Бакыта!\n{message.from_user.full_name}\n'
                             f'Отправьте мне фото блюда...',
                             reply_markup=cancel_markup)
    else:
        await message.reply('Нет полномочий! ты никто')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f'@{message.from_user.username}'
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Название блюда:')


async def load_name_food(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Описание блюда:')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer('Цена:')


async def load_food_cost(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['cost'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Энергетическая ценность:')
    except:
        await message.answer('only integer bitch')


async def load_energy_value(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['value'] = int(message.text)
            await bot.send_photo(message.from_user.id, data['photo'],
                                 caption=f'Name:{data["name"]}\n'
                                 f'About food:{data["description"]}\n'
                                 f'Cost:{data["cost"]} som\n'
                                 f'Energy value:{data["value"]}')
        await state.finish()
        await message.answer('Блюдо успешно добавлено!')
    except:
        await message.answer('only integer bitch')


async def quit_fsm(message: types.Message, state: FSMContext):
    state_status = await state.get_state()
    if state_status is None:
        return
    await state.finish()
    await message.answer('you have just quit from registration')


def register_handlers_fsmmenu(dp: Dispatcher):
    dp.register_message_handler(quit_fsm, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['add'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name_food, state=FSMAdmin.food_name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_food_cost, state=FSMAdmin.food_cost)
    dp.register_message_handler(load_energy_value, state=FSMAdmin.energy_value)
