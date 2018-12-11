import io
import itertools
import re
import subprocess
from threading import Thread

from core.data_extractor import DataExtractor
from core.objects.annotation import Annotation
from core.utils import ends_with_slash


class AnnotationsPageController:
    data_extractor: DataExtractor

    def view_annotation(self, anno_id):
        anno = self.data_extractor.get_tag(anno_id)

        file = self.data_extractor.get_book_file(anno.BookId)

        subpath = file.get_subpath()
        root_path = self.data_extractor.path

        page_num = int(re.findall("page=(\d+)", anno.Begin)[0]) + 1

        command = ["evince", "-p", str(page_num), ends_with_slash(root_path)+subpath]

        Thread(target=subprocess.check_call, args=[command], daemon=True).start()

    def annotations_as_markdown(self, **k)-> io.BytesIO:
        data = sorted(self.annotations(**k), key=lambda item: item.OID)

        s = io.StringIO()

        for item in data:
            s.write(f"\n\n{item.Text}")

        out = io.BytesIO()
        out.write(s.getvalue().encode("utf-8"))
        out.seek(0)
        s.close()

        return out

    def annotations(self, tag=None, bookId=None, **k):
        data = self.data_extractor.get_tags()

        def filterFunc(item: Annotation):
            bools = [True]
            if tag:
                bools.append(tag in item.TagName)
            if bookId:
                bools.append(item.BookId == int(bookId))

            if item.Text == "Bookmark":
                return False

            return all(bools)

        return list(filter(filterFunc, data))

    def books(self, **k):
        data = self.data_extractor.get_books()

        annotations = self.annotations(tag="bm.quotation")

        annotations_count = {}
        key = lambda a: a.BookId

        for bookId, group in itertools.groupby(
            sorted(annotations, key=key), key=key
        ):
            annotations_count[bookId] = len(list(group))

        for item in data:
            item.AnnotationsCount = annotations_count.get(item.OID, 0 )

        return sorted(data, key=lambda item: -item.AnnotationsCount)
