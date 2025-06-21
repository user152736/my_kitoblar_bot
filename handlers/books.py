from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, html
from database.database_connection import Books, session


books_router = Router()


@books_router.message(Command('books'))
async def command_start_handler(message: Message):
    books_list = session.query(Books).order_by(Books.id).all()

    itl = html.italic
    bl = html.bold

    lines = []
    for book in books_list:
        lines.append(f"{bl(book.id)}. {itl('sarlavha')}:{book.sarlavha}   {itl('muallif')}:{book.muallif}   {itl('janra')}:{book.janra}")

    await message.answer('\n'.join(lines))



