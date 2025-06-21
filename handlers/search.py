from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, html
from aiogram.fsm.context import FSMContext
from sqlalchemy import func

from state.search_state import SearchState
from database.database_connection import Books, session

search_router = Router()


@search_router.message(Command('search'))
async def command_start_handler(message: Message, state:FSMContext):
    await message.answer('qidirayotgan kitobingizning nomi, muallifi, yoki janrini kiriting')
    await state.set_state(SearchState.javob)


@search_router.message(SearchState.javob)
async def javob_state(message: Message):
    search_key = message.text

    results = session.query(Books).filter((func.lower(Books.sarlavha) == func.lower(search_key)) |
                                          (func.lower(Books.muallif) == func.lower(search_key)) |
                                          (func.lower(Books.janra) == func.lower(search_key))).order_by(Books.id).all()

    itl = html.italic
    bl = html.bold

    lines = []
    for result in results:
        lines.append(f"{bl(result.id)}. {itl('sarlavha')}:{result.sarlavha}   {itl('muallif')}:{result.muallif}   {itl('janra')}:{result.janra}")


    if lines:
        await message.answer('\n'.join(lines))
    else:
        await message.answer('siz qidirgan kitob bizning malumotlar bazasida mavjud emas 😞')



