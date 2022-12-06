from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from aiogram.dispatcher import Dispatcher
from utils.config import TOKEN_BOT

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)