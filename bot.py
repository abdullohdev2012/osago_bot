import logging

from aiogram import Bot, Dispatcher, executor, types
from btn import start_menu
from inline_btns import inline, inline_btn

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "6114940484:AAHPONhsn4xfh8hDm1tIMXmb3m1HehVg9B4"

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    menu = await start_menu()
    await message.answer("""
<b>🙋‍♀️Привет дорогой друг!
Меня зовут Осаго Макс</b>

Я был создан, чтобы помочь тебе оформить Электронный осаго и диагностические карты  на твой автомобиль.

<i>Обещаю не занимать у тебя много времени, <b>время = деньги</b>, поэтому все будет очень просто, быстро и максимально понятно.</i>

⏳Заказы обрабатываются: <b>с 09:00 до 22:00 по Московскому времени, а принимаются 24/7</b>

Выбери нужный пункт из меню и я с радостью тебе помогу😌""", reply_markup=menu)
    
@dp.message_handler(text="📂Наши услуги")
async def usluga_btn(message: types.Message):
    a = await inline()
    await message.answer("🌐Наши услуги", reply_markup=a)


@dp.message_handler(text="👤Профиль")
async def profil_btn(message: types.Message):
    b = await inline_btn()
    await message.answer("""
    👤 Ваш Профиль

🆔 ID: 5370726024
💰 Баланс: 0.0 руб.

Реф.ссылка: https://t.me/Osagoa_bot?start=5370726024""", reply_markup=b)

@dp.message_handler(text= "☎️Обратная связь")
async def svaz_bot(message:types.Message):
    await message.answer("✳️ Гл.Админ бота: @osagomaksc")

@dp.message_handler(text= "💥Телеграм канал")    
async def telegram_bot(message:types.Message):
    await message.answer(":✳️ Наш канал: @osagomak")

if __name__ == "__main__":
    executor.start_polling(dp)