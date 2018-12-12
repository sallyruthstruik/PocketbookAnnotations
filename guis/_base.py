import abc

from core.controller import AnnotationsPageController
from core.data_extractor import DataExtractor


class BaseGui(metaclass=abc.ABCMeta):

    def __init__(self, data_extractor: DataExtractor):
        self.data_extractor = data_extractor

        AnnotationsPageController.data_extractor = data_extractor

        from guis.browser.server import controller
        print(controller.data_extractor)

    @abc.abstractmethod
    def run(self):
        """
        Should run Gui interface
        """

