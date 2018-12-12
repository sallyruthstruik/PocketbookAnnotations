import logging
import socket
import webbrowser

from guis._base import BaseGui
from guis.browser.server import ServerProcess


class Gui(BaseGui):
    def run(self):
        # looking for port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for port in range(8000, 9000, 1):
            try:
                s.bind(("127.0.0.1", port))
                s.close()
                break
            except socket.error:
                continue
        else:
            logging.critical("No opened ports found!")
            return

        logging.info("Start server on port %s", port)
        pr = ServerProcess(port, self.data_extractor.path)
        pr.start()

        webbrowser.open(f"http://localhost:{port}")

        pr.join()
