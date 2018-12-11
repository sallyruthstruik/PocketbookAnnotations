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

    def get_subpath(self):
        out = self.Path.replace("/mnt/ext1", "") + self.Name
        if out[0] == "/":
            return out[1:]
        return out