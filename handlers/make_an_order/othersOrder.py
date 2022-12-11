from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
import utils.markap_menu as nv
import aiogram.utils.markdown as md
from create_bot import bot
from utils.statemachine import FAQ, OrderStates


async def started_order_handler(message: types.Message):
    if message.text == 'Сделать заказ':
        keyword_markup = types.InlineKeyboardMarkup(row_width=1)
        inline_btn = types.InlineKeyboardButton("FAQ", callback_data="faq")
        keyword_markup.add(inline_btn)
        await message.answer('Если возникнут трудности у нас хороший FAQ в разделе Консультаций',
                             reply_markup=keyword_markup)
        await message.answer('*Варианты доставки на Ваш выбор:*',
                             reply_markup=nv.SuperMenu.invoiceMenu,
                             parse_mode=ParseMode.MARKDOWN)


async def return_to_faq(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, md.text(
        md.text("Добро пожаловать в наш ", md.bold('FAQ'), "!"),
        md.text('По каждому из способов доставки мы имеем исчерпывающее руководство.'),
        md.text('Какой способ доставки вас интересует?'),
        sep='\n'),
                           reply_markup=nv.SuperMenu.faqMenu,
                           parse_mode=ParseMode.MARKDOWN)
    await FAQ.start.set()


async def switch_from_faq(query: types.CallbackQuery):
    print("it working")
    await OrderStates.order_kaz_choice.set()
    await bot.send_message(query.from_user.id, 'Отлично! Теперь нам нужно получить либо доступ'
                                               ' к корзине в магазине, '
                                               'либо прямые ссылки на товары. Выбор за вами:',
                           reply_markup=nv.SuperMenu.kaz_choice_menu)


def register_handlers_othersOrder(dp: Dispatcher):
    dp.register_message_handler(started_order_handler, Text(equals="Сделать заказ"), state="*")
    dp.register_callback_query_handler(switch_from_faq, text="Kazahstan")
    dp.register_callback_query_handler(return_to_faq, text="faq")

