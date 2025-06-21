import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import start_router, help_router, books_router, add_book_router, search_router
from helper_functions import menu_func

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.startup.register(menu_func)
    dp.include_routers(start_router, help_router, books_router, add_book_router, search_router)


    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

