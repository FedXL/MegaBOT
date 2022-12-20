from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode

import utils.markap_menu as nv
from utils.statemachine import Calculator_1, Calculator_2
from create_bot import usd,eur
import aiogram.utils.markdown as md


async def zero_calculator_handler(message: types.Message):
    if message.text == "Посчитать примерную стоимость заказа транзитом через Казахстан":
        await Calculator_1.eurobacs.set()
        await message.answer("Хорошо. Выберите теперь валюту для расчёта:", reply_markup=nv.SuperMenu.EuroBaksMenu)
    elif message.text == "Посчитать примерную стоимость по выкупу заказа":
        await Calculator_2.euro_usd.set()
        await message.answer("Хорошо. Выберите теперь валюту для расчёта:", reply_markup=nv.SuperMenu.EuroBaksMenu)


async def calculator_1(message: types.Message, state: FSMContext):
    if message.text in ("Евро", "Доллар"):
        await message.answer(f"Валюта: {message.text}, Теперь введите полную сумму корзины вместе"
                             f" с доставкой в Казахстан:",
                             reply_markup=nv.SuperMenu.cancel)
        await Calculator_1.getmoney.set()
        async with state.proxy() as data:
            data['eurobaks'] = message.text
    else:
        await message.reply("Непонятная команда, пожалуйста воспользуйтесь кнопками меню.")


async def getmoney1(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            valuta = data.get('eurobaks')
        if valuta == "Евро":
            valuta = eur
            pref = "Евро"
        elif valuta == "Доллар":
            valuta = usd
            pref = "Доллар"
        else:
            await message.answer(f"Что то пошло сильно не так. Валюта = {valuta}")
            return
    else:
        await message.answer(
            f"Предыдущее сообщение *{message.text}* не похоже на число. Число должно состоять"
            f" только из цифр, Попробуйте ещё раз.")
        return
    if int(message.text) > 1000:
        total1 = int(message.text) * 1.25 * valuta + 1000 + \
                 (int(message.text) - 1000) * 0.15 * 1.25 * valuta
        total2 = int(message.text) * 1.25 * valuta + 3000 + \
                 (int(message.text) - 1000) * 0.15 * 1.25 * valuta
        text1 = "Cумма к оплате вместе с таможенной пошлиной составит:"
    else:
        total1 = int(message.text) * 1.25 * valuta + 1000
        total2 = int(message.text) * 1.25 * valuta + 3000
        text1 = "Cумма к оплате составит:"
    await message.answer(md.text(
        md.text("Cумма="),
        md.text(" "),
        md.text("Cтоимость корзины с доставкой в Казахстан в валюте"),
        md.text("     x"),
        md.text(f"Биржевой курс валюты"),
        md.text("     x"),
        md.text("1.25 это наша комиссия и затраты на конвертацию"),
        md.text("     +"),
        md.text("Стоимость доставки в РФ (от 1000 руб. до 3000 руб.)"),
        md.text("     +"),
        md.text("Таможенное оформление , если сумма больше 1000 евро"),
        sep="\n"
    ))
    await message.answer(md.text(
        md.text(text1),
        md.text(" "),
        md.text(f"*от {total1} руб.*", f"*до {total2} руб.*", sep=" "),
        md.text(" "),
        md.text("В зависимости от габаритов и веса,"
                " влияет на стоимость доставки в Россию."),
        md.text(" "),
        md.text(f"*Курс валюты на сегодня: 1{pref} = {valuta} рублей.*"),
        md.text(" "),
        sep="\n"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=nv.SuperMenu.cancel)



async def calculator_2(message: types.Message, state: FSMContext):
    if message.text in ("Евро", "Доллар"):
        await message.answer(f"Валюта: {message.text}, Теперь введите полную сумму корзины вместе"
                             f" с доставкой:",
                             reply_markup=nv.SuperMenu.cancel)
        await Calculator_2.get_money.set()
        async with state.proxy() as data:
            data['eurobaks'] = message.text
    else:
        await message.reply("Непонятная команда, пожалуйста воспользуйтесь кнопками меню.")


# @dp.message_handler(state=Calculator_2.get_money)
async def getmoney2(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        async with state.proxy() as data:
            valuta = data.get('eurobaks')
        if valuta == "Евро":
            valuta = eur
            pref = "Евро"
        elif valuta == "Доллар":
            valuta = usd
            pref = "Доллар"
        else:
            await message.answer(f"Что то пошло сильно не так. Валюта = {valuta}")
            return
    else:
        await message.answer(
            f"Ничего не понимаю. Предыдущее сообщение *{message.text}* не похоже на число. Число должно состоять"
            f"только из цифр, Попробуйте ещё раз.")
        return

    if int(message.text) > 1000:
        total = int(message.text) * 1.2 * valuta
        text1 = "Cумма к оплате,без учета таможенной пошлины составит:"
    else:
        total = int(message.text) * 1.2 * valuta
        text1 = "Cумма к оплате составит:"
    await message.answer(md.text(
        md.text("Cумма="),
        md.text(" "),
        md.text("Cтоимость корзины с доставкой."),
        md.text("     x"),
        md.text(f"Биржевой курс валюты"),
        md.text("     x"),
        md.text("1.2 это наша комиссия и затраты на конвертацию"),
        sep="\n"
    ))
    await message.answer(md.text(
        md.text(text1),
        md.text(" "),
        md.text(f"* {int(total)} руб.*"),
        md.text(" "),
        md.text(f"*Курс валюты на сегодня: 1{pref} = {valuta} рублей.*"),
        sep="\n"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=nv.SuperMenu.cancel)

def register_handlers_calculator(dp: Dispatcher):
    dp.register_message_handler(zero_calculator_handler,
                                Text(equals=["Посчитать примерную стоимость заказа транзитом через Казахстан",
                                             "Посчитать примерную стоимость по выкупу заказа"]),
                                state="*")
    dp.register_message_handler(getmoney1, state=Calculator_1.getmoney),
    dp.register_message_handler(getmoney2, state=Calculator_2.get_money),
    dp.register_message_handler(calculator_1, state=Calculator_1.eurobacs),
    dp.register_message_handler(calculator_2, state=Calculator_2.euro_usd)