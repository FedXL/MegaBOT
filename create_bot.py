from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram.dispatcher import Dispatcher
from utils.config import API_TOKEN


logging.basicConfig(level=logging.DEBUG)
storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot,
                storage=storage)



