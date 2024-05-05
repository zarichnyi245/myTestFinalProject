import asyncio

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


from . routers import default_router, film_router

# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()


# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()
root_router.include_routers(default_router, film_router, )

async def pprint():
    while True:
        print("hello111")
        await asyncio.sleep(2)

async def main() -> None:
    # Дістанемо токен бота з середовища
    TOKEN = getenv("BOT_TOKEN")
    # Створимо об'єкт Bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    
    dp = Dispatcher()
    dp.include_router(root_router)
    # Почнемо обробляти події для бота
    await asyncio.create_task(pprint())
    await dp.start_polling(bot)



