import logging

logging.getLogger(__name__)


available_commands = dict() # "name : description"


def create_commands() -> None:
    d = dict()
    d['help'] = 'print this message'
    d['get'] = 'send all the wastings'

    available_commands.update(d)


def help_message():
    """ Reply message to /help command
    :returns: string with a help message
    """

    create_commands()

    help_string = "Message format: <i>sum category</i> (e.g. <i>'750 food'</i>)\n"
    for k, v in available_commands.items():
        help_string += f"/{k} -- {v}\n"
    logging.info(f"Help message: '{help_string}'")
    return help_string


def start_message():
    """ Reply message to /start command
    :returns: string with a start message
    """

    message_text = "Hello! Welcome to MoneyBot!"
 
    message_text += "Send a message with a wasted sum and category of wasting. "\
            "That sum will be written, you can get "\
            "a report of your wastings for exact period\n\n"
    message_text += help_message().strip() # add help msg to start_message
    logging.info(f"Start message: '{message_text}'")
    return message_text
