import logging
import marka as nv
import random
from texts import text_var_2_1

from exchange import get_exchange as valut
import aiogram.utils.markdown as md
from aiogram import executor, Bot, Dispatcher, types
from config import TOKEN_API,NAME
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ParseMode
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils import ShopValid


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)



class Deep0 (StatesGroup):
    lvl1 = State()
    lvl2 = State()

class Deep1_Consult(StatesGroup):
    lvl3 = State()
    lvl4 = State()
    lvl5 = State()
    lvl4 = State()
    lvl5 = State()
    lvl6 = State()





@dp.message_handler(commands=['start'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await state.finish()
    await bot.send_message(message.from_user.id, f"Здравcтсвуйте {md.bold(message.from_user.username)}!"    
                                                 f"Я бот помощник.\n")

@dp.message_handler(commands=['lvl4'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await Deep1_Consult.lvl4.set()
    await bot.send_message(message.from_user.id, f"Здравcтсвуйте я лвл 4"    
                                                 f"Я бот помощник.\n")



@dp.message_handler(commands=['next'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await Deep1_Consult.next()
    current_state = await state.get_state()
    print(current_state)
    print(type(current_state))
    await bot.send_message(message.from_user.id, f"Вперед  вы на уровне{current_state} ")




@dp.message_handler(commands=['back'], state="*")
async def welcome_message(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await Deep1_Consult.previous()
    current_state  = await state.get_state()
    print(Deep1_Consult.all_states)
    print(current_state)
    await bot.send_message(message.from_user.id, f"Назад вы на уровне {current_state}")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
