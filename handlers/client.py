from aiogram import Dispatcher, types
from create_bot import dp, bot
from database import sqlite_db
from keyboards import buttons_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id,
                               'Bon appetit!',
                               reply_markup=buttons_client)
        await message.delete()
    except:
        await message.reply('You need to write the Bot for interaction')


# @dp.message_handler(commands=['address'])
async def get_address(message: types.message):
    address = "Kabanbay batyr 53, Nur-Sultan"
    await bot.send_message(message.from_user.id, address)


# @dp.message_handler(commands=['hours'])
async def get_work_hours(message: types.message):
    work_hours = "8:00-23:45 everyday"
    await bot.send_message(message.from_user.id, work_hours)


async def get_menu(message: types.message):
    await sqlite_db.sqlite_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(get_address, commands=['address'])
    dp.register_message_handler(get_work_hours, commands=['hours'])
    dp.register_message_handler(get_menu, commands=['menu'])
