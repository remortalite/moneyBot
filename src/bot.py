import src.config as config
import src.messages as messages

from aiogram import Bot, Dispatcher, executor, types
import logging


logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def show_start_message(msg : types.Message):
    await msg.answer(text=messages.start_message())


@dp.message_handler(commands=['help'])
async def show_help_message(msg : types.Message):
    await msg.answer(text=messages.help_message())
