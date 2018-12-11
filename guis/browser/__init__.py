from guis._base import BaseGui
from guis.browser.server import ServerProcess


class Gui(BaseGui):
    def run(self):
        pr = ServerProcess()
        pr.run()
