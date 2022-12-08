from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from utils.config import NAME
import utils.markap_menu as nv


async def make_first_choise_consult (message: types.Message):
    await message.answer('Koнсультация', reply_markup=nv.SuperMenu.consMenu)


async def call_consultant (message: types.Message):
    await message.answer(f"Если наш FAQ не помог, то {NAME} ответит на все ваши вопросы.")


def register_handlers_othersCons(dp: Dispatcher):
    dp.register_message_handler(call_consultant, Text(equals="Вызов Консультанта"),state="*"),
    dp.register_message_handler(make_first_choise_consult, Text(equals="Koнсультация"), state=None)
