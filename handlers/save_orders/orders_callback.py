from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode
import aiogram.utils.markdown as md
from create_bot import bot
from utils.config import message_id
from utils.markap_menu import SuperMenu
from utils.texts import make_user_info_report, make_links_info_text, order_answer_vocabulary, get_additional_from_proxi


async def make_order_answer(query: CallbackQuery, state: FSMContext):
    await query.answer("Успешно")
    await query.message.delete_reply_markup()
    await query.message.delete()
    income = query.data
    user_info = make_user_info_report(query)
    pre_additional = order_answer_vocabulary(income)
    match income:
        case "KAZ_ORDER_LINKS":
            async with state.proxy() as data:
                addition = get_additional_from_proxi(data)
        case "KAZ_ORDER_CABINET":
            async with state.proxy() as data:
                addition = [
                    md.text('Магазин: ', f"<code>{data.get('shop')}</code>"),
                    md.text('Логин: ', f"<code>{data.get('log')}</code>"),
                    md.text('Пароль: ', f"<code>{data.get('pass')}</code>"),
                ]
        case "TRADEINN":
            async with state.proxy() as data:
                addition = [
                    md.text('Логин: ', f"<code>{data.get('login')}</code>"),
                    md.text("Пaроль: ", f"<code>{data.get('pass')}</code>")
                ]
        case "PAYMENT":
            async with state.proxy() as data:
                addition = [
                    md.text('Магазин: ', f"<code>{data.get('shop')}</code>"),
                    md.text('Логин: ', f"<code>{data.get('login')}</code>"),
                    md.text('Пароль: ', f"<code>{data.get('pass')}</code>"),
                ]
    await state.finish()
    await bot.send_message(query.from_user.id, md.text(
        md.text("Уважаемый", query.from_user.username, "!", sep=" "),
        md.text("Мы получили ваш заказ:"),
        sep="\n"))
    await bot.send_message(query.from_user.id, md.text(
        md.text(*pre_additional, sep="\n"),
        md.text(*addition, sep="\n"),
        sep="\n"),
                           reply_markup=SuperMenu.cancel,
                           disable_web_page_preview=True,
                           parse_mode=ParseMode.HTML)
    await bot.send_message(query.from_user.id, md.text("Ваш заказ будет обработан сегодня.",
                                                       "Скоро с вами свяжется наш специалист.", "@ShipKZ",
                                                       sep="\n"))
    await bot.send_message(message_id,
                           md.text(md.text(user_info),
                                   md.text(*addition, sep="\n"),
                                   sep="\n"),
                           disable_web_page_preview=True,
                           parse_mode=ParseMode.HTML)


def register_handlers_save_order(dp: Dispatcher):
    dp.register_callback_query_handler(make_order_answer,
                                       lambda c: c.data in ['KAZ_ORDER_LINKS', 'KAZ_ORDER_CABINET', 'TRADEINN',
                                                            'PAYMENT'],
                                       state="*")
