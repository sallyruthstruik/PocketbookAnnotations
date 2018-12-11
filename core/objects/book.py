from dataclasses import dataclass

from core.objects._base import BaseObject


@dataclass
class Book(BaseObject):
    OID: int
    Title: str
    Authors: str
    TimeAdd: int

    AnnotationsCount = 0

    def to_dict(self):
        out = super().to_dict()
        out["AnnotationsCount"] = self.AnnotationsCount
        return out
