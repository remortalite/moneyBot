import os
import logging

logging.getLogger(__name__)

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

if not BOT_API_TOKEN:
    logging.critical("Token cannot be taken from environment. "\
            "Please add environment variable BOT_API_TOKEN")
