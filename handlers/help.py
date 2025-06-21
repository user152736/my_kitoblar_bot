from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

help_router = Router()


@help_router.message(Command('help'))
async def command_start_handler(message: Message):
    await message.answer(f"umimiy salomlashish 👉 /start \n"
                         f"barchabuyruqlar va ularning vazifasi 👉 /help \n"
                         f"barcha kitoblar ro`yxati 👉 /books \n"
                         f"kitob qoshish 👉 /add_book \n"
                         f"kitoblarni qidirish buyrugi 👉 /search \n")

