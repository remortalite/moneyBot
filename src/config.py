import os
import logging

logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logging.critical("Token cannot be taken from environment. "\
            "Please add environment variable BOT_TOKEN")
