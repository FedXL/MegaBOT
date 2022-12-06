import logging
from utils import markap_menu as nv
import random
from utils.texts import make_text_hello, make_text_for_FAQ
from utils.exchange import get_exchange as valut
import aiogram.utils.markdown as md
from aiogram import executor, Bot, Dispatcher, types
from utils.config import NAME
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from utils import ShopValid

name = NAME

try:
    mas = valut()
    eur = (mas[1])
    usd = (mas[0])
except:
    eur = 666
    use = 666

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token='5739990172:AAF_gEttCevePt7p2Mi0og-er3XhQRQvcxg')
dp = Dispatcher(bot=bot,
                storage=storage)

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
    print(value)

















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
