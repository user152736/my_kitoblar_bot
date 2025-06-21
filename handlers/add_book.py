from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from state.add_book_state import BookAddState
from keybord.regular.button import confirm_button
from database.database_connection import Books, session


add_book_router = Router()


@add_book_router.message(Command('add_book'))
async def command_start_handler(message: Message, state:FSMContext):
    await state.set_state(BookAddState.sarlavha)
    await message.answer('kitob sarlavhasini kiriritng')


@add_book_router.message(BookAddState.sarlavha)
async def sarlavha_state(message: Message, state:FSMContext):
    await state.update_data(sarlavha= message.text)
    await state.set_state(BookAddState.muallif)
    await message.answer('kitob muallifini kiriting')

@add_book_router.message(BookAddState.muallif)
async def muallif_state(message: Message, state:FSMContext):
    await state.update_data(muallif= message.text)
    await state.set_state(BookAddState.janra)
    await message.answer('kitob janrasini kiriting')


@add_book_router.message(BookAddState.janra)
async def janra_state(message: Message, state:FSMContext):
    await state.update_data(janra= message.text)
    data = await state.get_data()
    await message.answer(f'kiritilgan malumotlarni tasdiqlang\n'
                         f'sarlavha: {data['sarlavha']}\n'
                         f'muallif: {data['muallif']}\n'
                         f'janra: {data['janra']}',
                         reply_markup=confirm_button())

    await state.set_state(BookAddState.confirm)


@add_book_router.message(BookAddState.confirm)
async def muallif_state(message: Message, state:FSMContext):
    if message.text == 'HA 🟢':
        data = await state.get_data()
        books = Books(sarlavha=data['sarlavha'], muallif=data['muallif'], janra=data['janra'])
        books.save(session)
        await message.answer('kitob malumotlari saqlandi', reply_markup=None)
    elif message.text == 'YO`Q 🔴':
        await message.answer('iltimos unda kitob malumotlarini qayta kiriting 👉 /add_book', reply_markup=None)


































