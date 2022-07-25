from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import sqlite_db
from keyboards import admin_kb


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def moder(message: types.message):
    await sqlite_db.add_moder(message.from_user.id, message.from_user.username)
    await bot.send_message(message.from_user.id,
                           "I am J.A.R.V.I.S.",
                           reply_markup=admin_kb.admin_buttons)
    await message.delete()


async def start_upload(message: types.message):
    global IDlist
    IDlist = await sqlite_db.get_moders_db()
    print(IDlist)
    for ID in IDlist:
        print(ID[0])
        if message.from_user.id == int(ID[0]):
            print("start upload")
            await FSMAdmin.photo.set()
            await message.reply('Send photo')


async def upload_pic(message: types.message, state: FSMContext):
    for ID in IDlist:
        if message.from_user.id == int(ID[0]):
            async with state.proxy() as data:
                data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply('Send name')


async def upload_name(message: types.message, state: FSMContext):
    for ID in IDlist:
        if message.from_user.id == int(ID[0]):
            async with state.proxy() as data:
                data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Send description')


async def upload_description(message: types.message, state: FSMContext):
    for ID in IDlist:
        if message.from_user.id == int(ID[0]):
            async with state.proxy() as data:
                data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Send price')


async def upload_price(message: types.message, state: FSMContext):
    for ID in IDlist:
        if message.from_user.id == int(ID[0]):
            async with state.proxy() as data:
                data['price'] = float(message.text)

            await sqlite_db.sqlite_upload(state)
            await message.reply('Successfully added!')
            await state.finish()


async def cancel(message: types.message, state: FSMContext):
    for ID in IDlist:
        if message.from_user.id == int(ID[0]):
            current_state = await state.get_state()
            if current_state == None:
                return
            await state.finish()
            await message.reply('Done')


async def callback_del(callback: types.callback_query):
    name = callback.data.replace('del ', '')
    await sqlite_db.sqlite_delete(name)
    await callback.answer(text=f'{name} was successfully deleted',
                          show_alert=True)


async def delete(message: types.message):
    IDlist = await sqlite_db.get_moders_db()

    for ID in IDlist:
        if message.from_user.id == int(ID[0]):
            data = await sqlite_db.sqlite_read2()
            for ret in data:
                await bot.send_photo(
                    message.from_user.id,
                    ret[0],
                    f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[3]}',
                    reply_markup=InlineKeyboardMarkup().add(
                        InlineKeyboardButton('Delete',
                                             callback_data=f'del {ret[1]}')))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start_upload, commands=['Upload'], state=None)
    dp.register_message_handler(upload_pic,
                                content_types=['photo'],
                                state=FSMAdmin.photo)
    dp.register_message_handler(upload_name, state=FSMAdmin.name)
    dp.register_message_handler(upload_description, state=FSMAdmin.description)
    dp.register_message_handler(upload_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel, commands=['cancel'], state='*')
    dp.register_message_handler(moder,
                                commands=['moderator'],
                                is_chat_admin=True)
    dp.register_callback_query_handler(
        callback_del, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete, commands=['Delete'])
