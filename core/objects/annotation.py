from dataclasses import dataclass
from core.objects._base import BaseObject


@dataclass
class Annotation(BaseObject):
    OID: int
    ItemId: int
    TagId: int
    Val: str
    TimeEdt: int

    TagNameOid: int
    TagName: str
    Opts: int
