import logging
import datetime

logging.getLogger(__name__)


def add_record(uid : int, time : datetime.datetime, money : int, category : str):
    """ Record saving (now it's working w/ file)
    :returns: None
    """
    with open(f"./user{uid}.csv", "a+") as f:
        logging.info(f"Saving the record '{time},{money},{category}'"\
                f" in file user{uid}.csv")
        f.write(f"{time},{money},{category}\n")
