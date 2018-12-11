import functools
import os
import sqlite3
import typing
from pprint import pprint

from core import utils, config
from core.objects.annotation import Annotation
from core.objects.book import Book
from core.objects.file import File


class DataExtractor:

    @classmethod
    def from_root(cls, path: str):
        return cls(path)

    def __init__(self, path: str)-> None:
        self.path = path

        try:
            self.cursor = sqlite3.connect(os.path.join(
                self.path, "system", "config", "books.db"
            ))
        except:
            utils.fatal("Can't open sqlite database. Check if path %s is correct and "
                        "subpath system/config/books.db exists")

    @functools.lru_cache(maxsize=config.cache_size)
    def get_tags(self)-> typing.List[Annotation]:
        d = self.cursor.execute("""
SELECT t.*, tn.*
FROM  Tags t JOIN TagNames tn ON t.TagID = tn.OID
        """)

        return [
            Annotation(*i)
            for i in d.fetchall()
        ]

    def get_tag(self):
        pass

    @functools.lru_cache(maxsize=config.cache_size)
    def get_book(self, oid: int)-> Book:
        cur_oid = oid
        while True:
            c = self.cursor.execute("""
SELECT OID, ParentID
FROM Items
WHERE OID = ?
            """, [cur_oid])

            cur_oid, parent_id = c.fetchone()
            if parent_id is None:
                break

            cur_oid = parent_id

        c = self.cursor.execute("SELECT * FROM Books WHERE OID = ?", [cur_oid]).fetchone()
        return Book(*c)

    @functools.lru_cache(maxsize=config.cache_size)
    def get_book_file(self, book_id: int):
        c = self.cursor.execute("""
SELECT f.*, p.*
FROM Files f JOIN Paths p ON f.PathID = p.OID WHERE BookID = ?
        """, [book_id])

        return File(*c.fetchone())


if __name__ == '__main__':
    de = DataExtractor.from_root("/home/skaledin/Dropbox/BACKUPS/PocketBook/")

    tags = de.get_tags()

    tagId = 6576

    tag = next(filter(lambda i: i.OID == tagId, de.get_tags()))

    book = de.get_book(tag.ItemId)
    file = de.get_book_file(book.OID)

    pprint([
        book,
        file,
        tag.Val,
    ])
