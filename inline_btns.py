from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

async def inline():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("📑купить OCAGA", callback_data="btn1")
    btn2 = InlineKeyboardButton("📋ТЕХОСМОТОР", callback_data="btn2")
    btn3 = InlineKeyboardButton("📸ФОТОШОП ТЕХОСМОТОР", callback_data="btn3")
    btn4 = InlineKeyboardButton("🏦КАСКО ДЛЯ БАНКА", callback_data="btn4")
    btn5 = InlineKeyboardButton("🏢КАРКА УЧЕТА ГИБДД", callback_data="btn5")
    btn6 = InlineKeyboardButton("🚗КАРТА ВУ ПОБАЗЕ ГАИ", callback_data="btn6")
    btn7 = InlineKeyboardButton("🔍ПОИСК ПО БАЗЕ СОЛЬЯРИС", callback_data="btn7")
    btn8 = InlineKeyboardButton("🏦ДЛЯ ВОССТАНОВЛЕНИЯКБМ", callback_data="btn8")
    btn9 = InlineKeyboardButton("🏷️ДОГОВОР КУПЛИ ПРОДАЖИ", callback_data="btn9")
    btn10 = InlineKeyboardButton("🖨️СНИЯТИЕ ТС С УЧЕТА", callback_data="btn10")

    inline_keyboard.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10)

    return inline_keyboard




async def inline_btn():
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("💳Пополнить баланс", callback_data="btn11")
    btn2 = InlineKeyboardButton("👜История заказов", callback_data="btn12")

    inline_keyboard.add(btn1,btn2,)

    return inline_keyboard
