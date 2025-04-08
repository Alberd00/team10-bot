from aiogram import types
from aiogram import F
from aiogram import Router

r = Router()

@r.callback_query(F.data == "button_callback")
async def button_message(callback: types.CallbackQuery):
    await callback.message.answer(f'Ты нажал на кнопку, {callback.from_user.username}')
