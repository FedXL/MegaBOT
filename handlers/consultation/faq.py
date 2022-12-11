from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from create_bot import usd, eur, bot
import aiogram.utils.markdown as md
from utils.statemachine import FAQ
from utils.texts import make_text_for_FAQ
import utils.markap_menu as nv


async def hello_faq(message: types.Message):
    await bot.send_message(message.from_user.id, md.text(
        md.text("Добро пожаловать в наш ", md.bold('FAQ'), "!"),
        md.text('По каждому из способов доставки мы имеем исчерпывающее руководство.'),
        md.text('Какой способ доставки вас интересует?'),
        sep='\n'),
                           reply_markup=nv.SuperMenu.faqMenu,
                           parse_mode=ParseMode.MARKDOWN)
    await FAQ.start.set()


# keyword_markup =
#         inline_btn = types.InlineKeyboardButton("FAQ", callback_data="faq")
#         keyword_markup.add(inline_btn)



async def generate_faq(message: types.Message):
    inl_menu = types.InlineKeyboardMarkup(row_width=1)
    if message.text == "Покупка транзитом через Казахстан":
        btn = types.InlineKeyboardButton("Зделать заказ", callback_data="Kazahstan")
        inl_menu.add(btn)
        await message.answer(make_text_for_FAQ(eur, usd, 'var_1_1'),
                             reply_markup=inl_menu,
                             parse_mode=ParseMode.MARKDOWN
                             )

        await message.answer(make_text_for_FAQ(eur, usd, 'var_1_2'),
                             reply_markup=nv.SuperMenu.faqMenu,
                             parse_mode=ParseMode.MARKDOWN
                             )
    elif message.text == "Покупка на Tradeinn":
        btn = types.InlineKeyboardButton("Зделать заказ", callback_data="TradeInn")
        inl_menu.add(btn)
        await message.answer(make_text_for_FAQ(eur, usd, 'var_2_1'),
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=inl_menu
                             )

        await message.answer(make_text_for_FAQ(eur, usd, 'var_2_2'),
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=nv.SuperMenu.faqMenu
                             )

    elif message.text == "Покупка через почтовых посредников":
        btn = types.InlineKeyboardButton("Зделать заказ", callback_data="Agent")
        inl_menu.add(btn)
        await message.answer(make_text_for_FAQ(eur, usd, 'var_3_1'),
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=inl_menu,
                             )

        await message.answer(make_text_for_FAQ(eur, usd, 'var_3_2'),
                             parse_mode=ParseMode.MARKDOWN,
                             reply_markup=nv.SuperMenu.faqMenu)
    else:
        await message.reply("Я такой команды не знаю! Используйте меню для выбора ответа.",
                            reply_markup=nv.SuperMenu.faqMenu)


def register_handlers_faq(dp: Dispatcher):
    dp.register_message_handler(hello_faq, Text(equals='FAQ'), state=None)
    dp.register_message_handler(generate_faq, state=FAQ.start)
