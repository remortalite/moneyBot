from src.messages import start_message
from src.utils import *
from src.bot import bot, dp

import logging
from aiogram import executor


def main():
    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
