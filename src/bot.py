import src.config as config
import src.messages as messages
import src.utils as utils

from aiogram import Bot, Dispatcher, executor, types
import logging
import datetime
import re


logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def show_start_message(msg : types.Message):
    await msg.answer(text=messages.start_message(), 
                     parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['help'])
async def show_help_message(msg : types.Message):
    await msg.answer(text=messages.help_message(),
                     parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=['getcsv'])
async def get_csv_command(msg : types.Message):
    await msg.reply_document(open(f"user{msg.from_id}.csv", "rb"))


@dp.message_handler(content_types=['text'])
async def save_record_message(msg : types.Message):
    regexp = r"^(\d+)\s+(\w+)$"
    if re.search(regexp, msg.text.strip()):
        match = re.match(regexp,  msg.text.strip())
        logging.info(f"Saving the record...")
        utils.add_record(msg.from_id, datetime.datetime.now(), match[1], match[2])
        await msg.reply(f"Saved: {match[1]} in category '{match[2]}'")
    else:
        await msg.reply(text="Incorrect format! Try using /help to see how to use this bot.")

