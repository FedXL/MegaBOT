from aiogram import types
from aiogram.contrib.middlewares import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, CallbackQuery
from aiogram.utils import executor
from create_bot import dp, bot
from handlers.make_an_order import var_1, othersOrder, var_2, var_3
from utils import markap_menu as nv
from handlers.back_btn import btn
from handlers.consultation import calculator,othersCons,faq
from utils.texts import make_text_hello


async def on_startup(_):
    print("Бот вышел в онлайн")


@dp.message_handler(commands=['start'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await state.finish()
    text = make_text_hello(message.from_user.username)
    await bot.send_message(message.from_user.id, text,
                           reply_markup=nv.SuperMenu.menu,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['info'], state="*")
async def info_func(message: types.Message, state: FSMContext):
    value = await state.get_state()
    print("state == ",value)




if __name__ == "__main__":
    btn.register_handlers_btn(dp)
    othersCons.register_handlers_othersCons(dp)
    othersOrder.register_handlers_othersOrder(dp)
    var_1.register_handlers_var_1(dp)
    var_2.register_handlers_var_2(dp)
    var_3.register_handlers_var_3(dp)
    calculator.register_handlers_calculator(dp)
    faq.register_handlers_faq(dp)
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup
                           )

