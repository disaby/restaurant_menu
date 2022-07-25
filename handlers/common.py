from create_bot import bot, dp
from aiogram import types, Dispatcher
import json, string


# @dp.message_handler()
async def echo(message: types.message):
    if {
            i.lower().translate(str.maketrans('', '', string.punctuation))
            for i in message.text.split(' ')
    }.intersection(set(json.load(open('prohibited.json')))) != set():
        await message.reply('Do not use prohibited words!')
        await message.delete()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(echo)