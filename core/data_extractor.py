import functools
import os
import sqlite3
import threading
import typing
from pprint import pprint

from core import utils, config
from core.objects.annotation import Annotation
from core.objects.book import Book
from core.objects.file import File

_threadlocal = threading.local()


class DataExtractor:

    @classmethod
    def from_root(cls, path: str):
        return cls(path)

    def __init__(self, path: str)-> None:
        self.path = path

        self.db_path = os.path.join(
            self.path, "system", "config", "books.db"
        )

        try:
            self._cursor = sqlite3.connect(self.db_path)
        except:
            utils.fatal("Can't open sqlite database. Check if path %s is correct and "
                        "subpath system/config/books.db exists")

    @property
    def cursor(self):
        if not hasattr(_threadlocal, "cursor"):
            _threadlocal.cursor = sqlite3.connect(self.db_path)

        return _threadlocal.cursor

    @functools.lru_cache(maxsize=config.cache_size)
    def get_tags(self)-> typing.List[Annotation]:
        d = self.cursor.execute("""
SELECT t.*, tn.*
FROM  Tags t JOIN TagNames tn ON t.TagID = tn.OID
ORDER BY t.TimeEdt DESC
        """)

        books = self.get_books()
        out = [
            Annotation(*i)
            for i in d.fetchall()
        ]
        parent_map = self._get_items_parent_map()

        for a in out:
            bookId = parent_map.get(a.ItemId, a.ItemId)

            try:
                book = next(filter(lambda b: b.OID == bookId, books))
            except:
                continue

            a.BookId = bookId
            a.BookTitle = book.Title

        return out

    def get_tag(self, tag_id):
        return next(filter(lambda item: item.OID == int(tag_id), self.get_tags()))

    @functools.lru_cache(maxsize=config.cache_size)
    def _get_items_parent_map(self)-> typing.Dict[int, int]:
        # map: childId - parentId
        cur = self.cursor.execute("SELECT OID, ParentId FROM Items ORDER BY OID")
        data = cur.fetchall()
        out = {}

        for child_id, parent_id in data:
            if parent_id:
                while parent_id in out and out[parent_id]:
                    parent_id = out[parent_id]

                out[child_id] = parent_id

        return out

    @functools.lru_cache(maxsize=config.cache_size)
    def get_books(self):
        c = self.cursor.execute("SELECT * FROM Books")
        c = c.fetchall()

        return [
            Book(*i)
            for i in c
        ]

    def annotations_count(self)-> typing.Dict[int, int]:
        # returns BookId, annotations count
        annotations = self.get_tags()

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

    from core.controller import AnnotationsPageController

    con = AnnotationsPageController()
    con.data_extractor = de
    con.view_annotation(tagId)


