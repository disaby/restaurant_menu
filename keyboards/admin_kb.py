from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

admin_buttons = ReplyKeyboardMarkup(resize_keyboard=True)

item1 = KeyboardButton('/Upload')
item2 = KeyboardButton('/Delete')

admin_buttons.add(item1, item2)
