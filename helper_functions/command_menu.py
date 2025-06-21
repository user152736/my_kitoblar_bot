from aiogram import Bot
from aiogram.types import BotCommand

async def menu_func(bot:Bot):
    menu_list = [
        BotCommand(command='/start', description='umimiy salomlashish'),
        BotCommand(command='/help', description='barchabuyruqlar va ularning vazifasi'),
        BotCommand(command='/books', description='barcha kitoblar ro`yxati'),
        BotCommand(command='/add_book', description='kitob qoshish'),
        BotCommand(command='/search', description='kitoblarni qidirish buyrugi')
    ]

    await bot.set_my_commands(menu_list)


    