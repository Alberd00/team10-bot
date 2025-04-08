from aiogram import Bot
from aiogram.types import BotCommand

command_list = [BotCommand(command="/start", description="Начало диалога с ботом"),
        BotCommand(command="/status", description="Вывод username и id пользователя"),
        BotCommand(command="/help", description="Информация о боте"),
        BotCommand(command="/button", description="Вызов кнопки")]

async def set_command_list(bot: Bot):

    await bot.set_my_commands(command_list)
