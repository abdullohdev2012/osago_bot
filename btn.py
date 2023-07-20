from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

async def start_menu():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.add(
        KeyboardButton("📂Наши услуги"),
        KeyboardButton("👤Профиль"),
        KeyboardButton("☎️Обратная связь"),
        KeyboardButton("💥Телеграм канал",)
    )
    return btn

