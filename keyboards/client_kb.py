from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

item1 = KeyboardButton("/address")
item2 = KeyboardButton("/hours")
item3 = KeyboardButton("/menu")
item4 = KeyboardButton("Send my contact", request_contact=True)
item5 = KeyboardButton("Send my location", request_location=True)

buttons_client = ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True)

buttons_client.add(item1, item2, item3).row(item4, item5)
