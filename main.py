from messages import start_message
from utils import *

import logging

bot = None


def main():
   start_message()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
