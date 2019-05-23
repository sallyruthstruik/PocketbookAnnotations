import shelve
import typing


class Storage:
    KEY_PROCESSED_ANNOTATIONS = "processed_annotations"

    def __init__(self):
        self.sh = shelve.open("storage.data")

    def __del__(self):
        self.sh.close()

    def get_processed_annotations(self) -> typing.Set[int]:
        return set(self.sh.get(self.KEY_PROCESSED_ANNOTATIONS, []))
