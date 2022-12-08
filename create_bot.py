from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram.dispatcher import Dispatcher
from utils.config import TOKEN_BOT
from utils.exchange import get_exchange

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot=bot,
                storage=storage)

money_rate = get_exchange()
usd = money_rate.usd
eur = money_rate.eur
m_date = money_rate.date

print("IMPORT CREATE BOT")