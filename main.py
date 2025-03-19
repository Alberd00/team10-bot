# version 0.1.0
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def process_start_command(message):
    await message.answer(f"Привет, {message.from_user.full_name} !")

@dp.message()
async def echo_handler(message):
    try:
        await message.answer(message.text)
    except:
        await message.answer("Попробуй снова!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())