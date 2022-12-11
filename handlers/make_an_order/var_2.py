import random
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
import utils.markap_menu as nv
import aiogram.utils.markdown as md

from create_bot import bot
from utils.statemachine import TradeInn


"""----------------------------ЗАКАЗ ЧЕРЕЗ traideINN"""

# @dp.message_handler(Text(equals='Заказ Tradeinn'), state=None)
async def start_tradeinn(message: types.Message):
    await message.answer("Прекрасно! Тогда понадобится логин и пароль от вашего личного кабинета на Tradeinn")
    await TradeInn.login.set()
    await message.answer('Введите логин: ', reply_markup=nv.SuperMenu.cancel)

async def switch_from_faq(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id,"Прекрасно! Тогда понадобится логин и пароль от вашего личного кабинета на Tradeinn")
    await TradeInn.login.set()
    await bot.send_message(query.from_user.id,
                           'Введите логин: ',
                           reply_markup=nv.SuperMenu.cancel)
# @dp.message_handler(state=TradeInn.login)
async def get_tradeinn_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await message.answer("Ваш логин сохранен!")
    await message.answer("Введите пароль", reply_markup=nv.SuperMenu.cancel)
    await TradeInn.pas.set()


# @dp.message_handler(state=TradeInn.pas)
async def get_tradeinn_pass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pass'] = message.text
    await message.answer("Ваш заказ отправлен! Скоро с вами свяжется оператор.")
    await message.answer(md.text(
        md.text(md.italic('TradeInn')),
        md.text('Номер заказа:', md.code(random.randint(1000, 9999))),
        md.text('Логин: ', md.bold(data.get('login'))),
        md.text("Пaроль:", md.bold(data.get('pass'))),
        sep='\n'),
        parse_mode=ParseMode.MARKDOWN)
    await state.finish()

def register_handlers_var_2(dp: Dispatcher):
    dp.register_message_handler(start_tradeinn, Text(equals='Заказ Tradeinn'), state=None)
    dp.register_message_handler(get_tradeinn_login, state=TradeInn.login)
    dp.register_message_handler(get_tradeinn_pass, state=TradeInn.pas)
    dp.register_callback_query_handler(switch_from_faq, text="TadeInn")

