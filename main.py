# version 2.1.0

from config import TOKEN
from aiogram import Bot, Dispatcher
import asyncio
import logging
from handlers.bot_commands import set_command_list
from handlers import handlers, callbacks
import sys
from utils import setup_logger


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(handlers.r)
    dp.include_router(callbacks.r)
    dp.startup.register(set_command_list)

    #logging.basicConfig(level=logging.INFO)
    setup_logger(fname=__name__)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
