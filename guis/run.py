import logging
import os
import sys
import click
import importlib

sys.path.append(os.path.abspath(os.path.curdir))

from core.data_extractor import DataExtractor
from guis._base import BaseGui


@click.command()
@click.argument("ui_name")
@click.argument("path")
def main(ui_name, path):
    logging.basicConfig(level="INFO")
    mod = importlib.import_module(f"guis.{ui_name}")

    data_extractor = DataExtractor.from_root(path)

    gui: BaseGui = mod.Gui(data_extractor)

    gui.run()


if __name__ == '__main__':
    main()
