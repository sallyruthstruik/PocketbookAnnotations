import logging
from json import JSONEncoder

from core.objects._base import BaseObject


def fatal(msg, *a, **k):
    logging.fatal(msg, *a, **k)
    exit(1)


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseObject):
            return o.to_dict()
        elif isinstance(o, bytes):
            return o.decode("utf8", errors="ignore")
        return super().default(o)
