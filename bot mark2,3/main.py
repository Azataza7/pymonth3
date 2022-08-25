
from aiogram.utils import executor
from config import dp
import logging
from handlers import client
from handlers import callback
from handlers import extra, fsmAdminMenu

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)
extra.register_message_handler_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

