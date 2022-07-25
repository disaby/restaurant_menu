from aiogram.utils import executor  #   bot execution for online
from create_bot import dp
from database import sqlite_db


async def on_startup(_):
    print("Bot online")
    sqlite_db.sqlite_start()


from handlers import client, admin, common

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
common.register_handlers_common(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
