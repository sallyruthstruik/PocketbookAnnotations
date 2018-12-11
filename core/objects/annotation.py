import json

from dataclasses import dataclass, field
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

    BookId: int = field(default=0)
    BookTitle: str = field(default="")

    Text = ""
    Begin = ""
    End = ""

    def __post_init__(self):
        try:
            parsed = json.loads(self.Val)
            self.Text = parsed.get("text", "").replace("-\n", "")
            self.Begin = parsed.get("begin", "")
            self.End = parsed.get("end", "")
            print(self.Text)
        except:
            pass

    def to_dict(self):
        out = super(Annotation, self).to_dict()
        out["Text"] = self.Text
        out["Begin"] = self.Begin
        out["End"] = self.End
        return out
