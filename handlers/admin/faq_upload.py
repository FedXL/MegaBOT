from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, Message, ReplyKeyboardRemove
from create_bot import bot
from utils.config import ADMINS
from utils.markap_menu import SuperMenu
from utils.statemachine import Admin


async def welcome_to_admin_mode(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, f"Вы в admin mode\n"
                                                     f"Для выхода введите /start\n"
                                                     f"Ловлю FAQ message")
        await Admin.admin.set()
    else:
        await bot.send_message(message.from_user.id,'Отказано в доступе')


async def welcome_message(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    with open("storages.html", "r") as fi:
        text = fi.read()
        fi.close()
    await bot.send_message(message.from_user.id, text,
                           reply_markup=SuperMenu.menu,
                           parse_mode=ParseMode.HTML)
    await Admin.admin.set()



async def catch_faq(message: Message):
    text = message.html_text
    string = text.split("\n")[0].lower()
    if "3 вариант" in string:
        variant = "faq_3"
    elif "2 вариант" in string:
        variant = "faq_2"
    elif "1 вариант" in string:
        variant = "faq_1"
    else:
        variant = "Фигня какая то давай те руками"
        await message.answer(variant)
        return
    print(variant)
    await message.answer(f"Сохраню как вариант {variant}")
    await bot.send_message(message.from_user.id,variant)

    with open("storages"+variant+".html", "w+", ) as fi:
        fi.write(text)
        fi.close()
    await message.answer("text is uploaded")


def register_handlers_upload_faq(dp: Dispatcher):
    dp.register_message_handler(welcome_to_admin_mode, commands=['admin'], state="*")
    dp.register_message_handler(catch_faq, state=Admin.admin)
