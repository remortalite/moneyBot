import logging

bot = None

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

    help_string = ""
    for k, v in available_commands.items():
        help_string += f"/{k} -- {v}\n"
    logging.info(f"Help message: '{help_string}'")
    return help_string


def start_message():
    """ Reply message to /start command
    :returns: string with a start message
    """
    
    message_text = "Hello! Welcome to MoneyBot!"
    message_text += "\n\n" + help_message().strip() # add help msg to start_message
    logging.info(f"Start message: '{message_text}'")
    return message_text


def add_record(money : int, category : str):
    """ TODO : add record saving
    :returns: None
    """
    pass


def main():
   create_commands() 
   start_message()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
