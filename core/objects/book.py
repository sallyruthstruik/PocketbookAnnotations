from dataclasses import dataclass

from core.objects._base import BaseObject


@dataclass
class Book(BaseObject):
    OID: int
    Title: str
    Authors: str
    TimeAdd: int
