from src.messages import start_message
from src.utils import *
from src.bot import bot

import logging


def main():
   start_message()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
