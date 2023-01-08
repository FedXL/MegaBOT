import logging

from aiogram import Dispatcher, types
from aiogram.types import ParseMode

from create_bot import bot
import aiogram.utils.markdown as md
from utils.config import rubbish
from utils.texts import make_user_info_report_from_message


async def warning (message: types.Message):

    user_id = message.from_user.id
    user_name = message.from_user.username
    text = message.text
    text_info=make_user_info_report_from_message(message)
    logging.info("send warning message")
    await bot.send_message(rubbish, md.text(
        text_info,
        "Писатель:",
        md.text(text),
        sep="\n"),
        parse_mode=ParseMode.HTML
        )
    await message.reply("Я вас не понимаю. Пожалуйста, воспользуйтесь кнопками меню.")
    await message.answer("Для перезапуска бота нажмите /start. Или верните меню.")


def register_handlers_warning(dp: Dispatcher):
    dp.register_message_handler(warning)
