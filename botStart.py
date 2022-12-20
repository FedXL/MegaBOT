from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.utils import executor
from create_bot import dp, bot
from handlers.back_btn.btn import register_handlers_btn
from handlers.consultation.calculator import register_handlers_calculator
from handlers.consultation.faq import register_handlers_faq
from handlers.consultation.othersCons import register_handlers_othersCons
from handlers.make_an_order.othersOrder import register_handlers_othersOrder
from handlers.make_an_order.var_1 import register_handlers_var_1
from handlers.make_an_order.var_2 import register_handlers_var_2
from handlers.make_an_order.var_3 import register_handlers_var_3
from handlers.save_orders.orders_callback import register_handlers_save_order
from utils import markap_menu as nv


from utils.texts import make_text_hello


async def on_startup(_):
    print("Бот вышел в онлайн")


@dp.message_handler(commands=['start'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # await message.reply(message.chat.id)
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
    register_handlers_save_order(dp)
    register_handlers_btn(dp)
    register_handlers_othersCons(dp)
    register_handlers_othersOrder(dp)
    register_handlers_var_1(dp)
    register_handlers_var_2(dp)
    register_handlers_var_3(dp)
    register_handlers_calculator(dp)
    register_handlers_faq(dp)
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup
                           )

