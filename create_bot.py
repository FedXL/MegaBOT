from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram.dispatcher import Dispatcher
from utils.config import API_TOKEN
from utils.exchange import get_exchange

logging.basicConfig(level=logging.DEBUG)
storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot,
                storage=storage)

money_rate = get_exchange()
usd = money_rate.usd
eur = money_rate.eur
m_date = money_rate.date

print("IMPORT CREATE BOT")