import logging
from aiogram import Bot, Dispatcher, executor
from config import TELEGRAM_BOT_TOKEN
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)