from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode
import aiogram.utils.markdown as md
from create_bot import bot
from utils.config import message_id
from utils.markap_menu import SuperMenu
from utils.texts import make_user_info_report, make_links_info_text


async def make_order_answer(query: CallbackQuery, state: FSMContext):
    await query.answer("Успешно")
    await query.message.delete_reply_markup()
    await query.message.delete()
    income = query.data
    user_info = make_user_info_report(query)
    match income:
        case "KAZ_ORDER_LINKS":
            async with state.proxy() as data:
                hrefs = [data.get(key) for key in
                         [('href_' + str(key)) for key in
                          [i for i in range(1, data.get('num') + 1)]]]
                addition = make_links_info_text(hrefs)
        case "KAZ_ORDER_CABINET":
            async with state.proxy() as data:
                addition = [
                    md.text('Магазин: ', md.bold(data['shop'])),
                    md.text('Логин:   ', md.bold(data['log'])),
                    md.text('Пароль:  ', md.bold(data['pass']))
                ]
        case "TRADE_INN":
            async with state.proxy() as data:
                addition = [
                    md.text('Логин: ', md.bold(data.get('login'))),
                    md.text("Пaроль: ", md.bold(data.get('pass')))
                ]
    await state.finish()
    await bot.send_message(query.from_user.id,md.text(
                           "Успешно! Номер вашего заказа *666*",
                           "Мы свяжемся с вами для уточнения деталей и оплаты.",
                            md.text(*addition,sep="\n"),
                            sep="\n"),
                           reply_markup=SuperMenu.cancel,
                           parse_mode=ParseMode.MARKDOWN)
    await bot.send_message(message_id,
                           md.text(md.text(user_info),
                                   md.text(*addition, sep="\n"),
                                   sep="\n"),
                           parse_mode=ParseMode.MARKDOWN)


def register_handlers_save_order(dp: Dispatcher):
    dp.register_callback_query_handler(make_order_answer,
                                       lambda c: c.data in ['KAZ_ORDER_LINKS', 'KAZ_ORDER_CABINET','TRADE_INN'],
                                       state="*")
