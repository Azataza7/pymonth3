
from aiogram.utils import executor
from config import dp
import logging

from database.bot_db import sql_create
from handlers import client
from handlers import callback
from handlers import extra, fsmAdminMenu,notifications
from database import bot_db
import asyncio


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)
notifications.register_handlers_notification(dp)

extra.register_message_handler_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

