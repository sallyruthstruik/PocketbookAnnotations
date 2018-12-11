import logging


def fatal(msg, *a, **k):
    logging.fatal(msg, *a, **k)
    exit(1)
