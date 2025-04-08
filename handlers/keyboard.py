from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def button_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Кнопка",callback_data="button_callback"))
    return builder.as_markup()
