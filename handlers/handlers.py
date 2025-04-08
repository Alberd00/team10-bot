from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import logging

r = Router()

@r.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}")
    logging.info(f"user {message.from_user.id} starts bot ")

@r.message(Command("status"))
async def status(message: Message):
    await message.answer(f"Username пользователя - {message.from_user.username}\nId пользователя - {message.from_user.id}")
    logging.info(f"user {message.from_user.id} chose status")

@r.message(Command("help"))
async def help(message: Message):
    await message.answer("Это бот для образовательных целей!)\nРазработчики - команда 10 \nСписок команд:\nstart - запуск бота\nhelp - информация о боте\nstatus - вывод Id и Username пользователя\nbutton - вывод сообщения с кнопкой")
    logging.info(f"user {message.from_user.id} chose help")

from handlers.keyboard import button_keyboard

@r.message(Command("button"))
async def button(message: types.Message):
    await message.answer(text="Нажмите на кнопку !)",reply_markup=button_keyboard())
    logging.info(f"user {message.from_user.id} chose button")

@r.message()
async def echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        logging.info(f"user {message.from_user.id} leaves unhandled message")
    except TypeError:
        await message.answer("Хорошая попытка!)")
        logging.info(f"user {message.from_user.id} leaves unhandled message with error")
