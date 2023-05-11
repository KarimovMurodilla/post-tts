from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.connection import Database
from utils.misc.tts.muxlisa import Muxlisa


# AIOgram
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# DB
db = Database()


# TTS
tts = Muxlisa()