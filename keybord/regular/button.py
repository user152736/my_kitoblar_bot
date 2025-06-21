from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def confirm_button():
    button = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='HA 🟢'),
                KeyboardButton(text='YO`Q 🔴')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return button