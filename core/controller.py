import itertools

from core.data_extractor import DataExtractor
from core.objects.annotation import Annotation


class AnnotationsPageController:
    data_extractor: DataExtractor

    def annotations(self, tag=None, bookId=None, **k):
        data = self.data_extractor.get_tags()

        def filterFunc(item: Annotation):
            bools = [True]
            if tag:
                bools.append(tag in item.TagName)
            if bookId:
                bools.append(item.BookId == int(bookId))

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
