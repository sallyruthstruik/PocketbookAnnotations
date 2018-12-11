from dataclasses import dataclass

from core.objects._base import BaseObject


@dataclass
class File(BaseObject):
    OID: int
    BookID: int
    PathID: int
    Name: str
    Len: int
    Ord: int

    PathOid: int
    StorId: int
    Path: str
